"""
tratamento.py · DataSUSpeitos (FMU Tech Inovação 2026.2 · ODS 3)

Lê as bases brutas (TabNet/SINASC e Painel de Indicadores de Sífilis), limpa, junta pelo
código IBGE e grava a tabela final: uma linha por município de SP × ano.

Entrada  (pasta data/raw/):
  - TabNet SINASC SP - consultas pre-natal por municipio - AAAA.csv   (um por ano)
  - painelSifilis.xlsx
Saída:
  - data/processed/tabela_final.csv

Como rodar (na pasta raiz do repositório):
  python src/tratamento.py
"""

# [A] Imports e configurações ---------------------------------------------------------
from io import StringIO
from pathlib import Path
import sys

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent          # pasta raiz do repositório
PASTA_RAW = RAIZ / "data" / "raw"
SAIDA = RAIZ / "data" / "processed" / "tabela_final.csv"

ANOS = [2019, 2020, 2021, 2022, 2023]                   # recorte aprovado pelo mentor
MIN_NV_RANKING = 1000                                   # filtro do ranking (ver dicionário)
ARQ_TABNET = "TabNet SINASC SP - consultas pre-natal por municipio - {ano}.csv"
ARQ_SIFILIS = "painelSifilis.xlsx"


# [B] Leitura de um CSV do TabNet ----------------------------------------------------
def ler_tabnet(ano: int) -> pd.DataFrame:
    """Lê o CSV de um ano e devolve: cod_ibge, ano e as contagens de pré-natal."""
    caminho = PASTA_RAW / ARQ_TABNET.format(ano=ano)

    # O arquivo pode vir de dois jeitos: baixado do TabNet (acentuação latin-1) ou copiado
    # da tela e colado no Bloco de Notas (UTF-8, com texto extra antes e depois da tabela).
    # Tenta UTF-8 primeiro; se falhar, usa latin-1.
    bruto = caminho.read_bytes()
    try:
        texto = bruto.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = bruto.decode("latin-1")

    # Recorta só a tabela: da linha do cabeçalho ("Município";...) até a linha antes de "Total".
    linhas = texto.splitlines()
    inicio = next(i for i, l in enumerate(linhas) if l.startswith('"Município";'))
    fim = next(i for i, l in enumerate(linhas) if l.startswith('"Total";'))
    df = pd.read_csv(StringIO("\n".join(linhas[inicio:fim])),
                     sep=";",      # o TabNet separa colunas com ponto e vírgula
                     dtype=str)    # lê tudo como texto; convertemos depois, com controle

    # Só ficam linhas de município: começam com 6 dígitos e um espaço ("350010 ADAMANTINA").
    # Isso descarta "MUNICIPIO IGNORADO", a linha "Total" e as notas do rodapé.
    df = df[df["Município"].str.match(r"^\d{6} ", na=False)].copy()
    df["cod_ibge"] = df["Município"].str[:6]

    # No TabNet, zero aparece como "-". Troca por 0 e converte para número inteiro.
    contagens = ["Nenhuma", "De 1 a 3 consultas", "De 4 a 6 consultas",
                 "7 ou mais consultas", "Ignorado", "Total"]
    for col in contagens:
        df[col] = pd.to_numeric(df[col].replace("-", "0")).astype(int)

    # Conferência de integridade: as 5 faixas de consultas somam o Total em toda linha.
    # Se não somarem, o arquivo foi cortado ou colado errado.
    if not df[contagens[:-1]].sum(axis=1).eq(df["Total"]).all():
        sys.exit(f"ERRO: no TabNet de {ano}, as faixas de consultas não somam o Total. Baixe/cole de novo.")

    df["ano"] = ano
    df["nascidos_vivos"] = df["Total"]
    df["nv_consultas_informadas"] = df["Total"] - df["Ignorado"]
    df["nv_menos_7_consultas"] = df["Nenhuma"] + df["De 1 a 3 consultas"] + df["De 4 a 6 consultas"]
    return df[["cod_ibge", "ano", "nascidos_vivos", "nv_consultas_informadas", "nv_menos_7_consultas"]]


# [C] Leitura da planilha de sífilis -------------------------------------------------
def ler_aba_sifilis(aba: str, prefixo: str, nome_saida: str) -> pd.DataFrame:
    """Lê uma aba do painel e devolve formato longo: cod_ibge, municipio, ano, <nome_saida>.

    Na planilha, cada ano é uma coluna ("<prefixo> 2019", "<prefixo> 2020"...).
    Para juntar com o TabNet, precisamos de uma linha por município × ano ("formato longo").
    """
    colunas = ["Código", "Nome Município"] + [f"{prefixo} {a}" for a in ANOS]
    df = pd.read_excel(PASTA_RAW / ARQ_SIFILIS, sheet_name=aba,
                       header=1,              # linha 1 da planilha só tem números 0, 1, 2...
                       usecols=colunas)

    # O código chega como decimal (353440.0). Vira inteiro e depois texto: "353440".
    df = df[df["Código"].notna()].copy()
    df["cod_ibge"] = df["Código"].astype(int).astype(str)

    # Só municípios de SP: 6 dígitos começando com 35. Descarta estado, regiões e Brasil.
    df = df[df["cod_ibge"].str.len().eq(6) & df["cod_ibge"].str.startswith("35")]

    longo = df.melt(id_vars=["cod_ibge", "Nome Município"],
                    value_vars=[f"{prefixo} {a}" for a in ANOS],
                    var_name="coluna", value_name=nome_saida)
    longo["ano"] = longo["coluna"].str[-4:].astype(int)
    longo[nome_saida] = longo[nome_saida].fillna(0).astype(int)
    return longo.rename(columns={"Nome Município": "municipio"})[
        ["cod_ibge", "municipio", "ano", nome_saida]]


# [D] Montagem da tabela final -------------------------------------------------------
def montar_tabela() -> pd.DataFrame:
    anos_disponiveis = [a for a in ANOS if (PASTA_RAW / ARQ_TABNET.format(ano=a)).exists()]
    faltando = sorted(set(ANOS) - set(anos_disponiveis))
    if faltando:
        print(f"AVISO: faltam os CSVs do TabNet de {faltando}. A tabela sai só com {anos_disponiveis}.")

    casos = ler_aba_sifilis("DADOS CONTINUAÇÃO 2",
                            "Sífilis congênita em menores de um ano", "casos_sc")
    diag = ler_aba_sifilis("DADOS CONTINUAÇÃO 4",
                           "Durante o pré-natal", "casos_sc_diag_prenatal")
    sifilis = casos.merge(diag[["cod_ibge", "ano", "casos_sc_diag_prenatal"]],
                          on=["cod_ibge", "ano"], how="left")
    sifilis = sifilis[sifilis["ano"].isin(anos_disponiveis)]

    prenatal = pd.concat([ler_tabnet(a) for a in anos_disponiveis], ignore_index=True)

    # A lista-base de municípios vem do painel (645). Junção "left": todo município do painel
    # fica, mesmo sem linha no TabNet. Quem não aparece no TabNet teve zero nascimentos
    # no ano (ex.: Borá em 2023) e recebe 0.
    tabela = sifilis.merge(prenatal, on=["cod_ibge", "ano"], how="left")
    sem_nascimentos = tabela["nascidos_vivos"].isna().sum()
    if sem_nascimentos:
        print(f"Info: {sem_nascimentos} município(s)-ano sem linha no TabNet → nascidos vivos = 0.")
    for col in ["nascidos_vivos", "nv_consultas_informadas", "nv_menos_7_consultas"]:
        tabela[col] = tabela[col].fillna(0).astype(int)

    # Município do TabNet que não existe no painel seria perdido em silêncio: avisa.
    perdidos = set(prenatal["cod_ibge"]) - set(tabela["cod_ibge"])
    if perdidos:
        print(f"AVISO: códigos do TabNet que não existem no painel: {sorted(perdidos)}")

    tabela["elegivel_ranking"] = tabela["nascidos_vivos"] >= MIN_NV_RANKING

    ordem = ["cod_ibge", "municipio", "ano", "nascidos_vivos", "nv_consultas_informadas",
             "nv_menos_7_consultas", "casos_sc", "casos_sc_diag_prenatal", "elegivel_ranking"]
    return tabela[ordem].sort_values(["ano", "cod_ibge"]).reset_index(drop=True)


# [E] Verificações automáticas (param o script se algo estiver errado) ------------------
def verificar(t: pd.DataFrame) -> None:
    erros = []
    if t.duplicated(["cod_ibge", "ano"]).any():
        erros.append("há linhas repetidas de cod_ibge + ano")
    if not t.groupby("ano")["cod_ibge"].nunique().eq(645).all():
        erros.append("algum ano não tem os 645 municípios de SP")
    if (t["nv_menos_7_consultas"] > t["nv_consultas_informadas"]).any():
        erros.append("menos de 7 consultas maior que consultas informadas")
    if (t["casos_sc_diag_prenatal"] > t["casos_sc"]).any():
        erros.append("diagnosticados no pré-natal maior que o total de casos")

    # Gabarito: números-chave conferidos pelo grupo (estado de SP, 2023)
    if 2023 in t["ano"].values:
        sp = t[t["ano"] == 2023].sum(numeric_only=True)
        pct = sp["nv_menos_7_consultas"] / sp["nv_consultas_informadas"] * 100
        taxa = sp["casos_sc"] / sp["nascidos_vivos"] * 1000
        print(f"Conferência SP 2023: {pct:.1f}% com menos de 7 consultas (gabarito 17,1%) · "
              f"{taxa:.1f} casos por mil NV (gabarito 8,5) · {int(sp['casos_sc'])} casos (gabarito 4.276)")
        if abs(pct - 17.1) > 0.1 or abs(taxa - 8.5) > 0.1:
            erros.append("os números de SP 2023 não batem com o gabarito")

    if erros:
        sys.exit("ERRO: " + "; ".join(erros))
    print("Verificações OK.")


# [F] Execução -------------------------------------------------------------------------
if __name__ == "__main__":
    tabela = montar_tabela()
    verificar(tabela)
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    tabela.to_csv(SAIDA, index=False, encoding="utf-8")
    print(f"Tabela final salva em {SAIDA.relative_to(RAIZ)} · {len(tabela)} linhas")
