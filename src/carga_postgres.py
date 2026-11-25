"""
carga_postgres.py · DataSUSpeitos (FMU Tech Inovação 2026.2 · ODS 3)

Carrega a tabela final (data/processed/tabela_final.csv) no PostgreSQL.
É o "L" (load) do pipeline: tratamento.py prepara os dados, este script guarda no banco.

Antes de rodar:
  1. PostgreSQL instalado e um banco chamado datasuspeitos criado
  2. Copiar .env.example para .env e preencher com o acesso ao seu banco

Como rodar (na pasta raiz do repositório):
  python src/carga_postgres.py
"""

# [A] Imports e configurações ---------------------------------------------------------
import os
from pathlib import Path
import sys

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

RAIZ = Path(__file__).resolve().parent.parent
CSV_FINAL = RAIZ / "data" / "processed" / "tabela_final.csv"
SQL_CRIAR = RAIZ / "sql" / "criar_tabela.sql"
TABELA = "fato_municipio_ano"


# [B] Conexão com o banco (os dados de acesso vêm do arquivo .env) ----------------------
def conectar():
    load_dotenv(RAIZ / ".env")            # lê o .env e coloca os valores no ambiente
    faltando = [v for v in ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]
                if not os.getenv(v)]
    if faltando:
        sys.exit(f"ERRO: faltam no arquivo .env: {faltando}. Copie o .env.example para .env e preencha.")

    url = URL.create(                     # monta o "endereço" do banco com segurança
        drivername="postgresql+psycopg2",
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    return create_engine(url)


# [C] Carga: cria a tabela (se não existir), apaga o conteúdo antigo e insere o novo ----
def carregar(engine) -> int:
    tabela = pd.read_csv(CSV_FINAL, dtype={"cod_ibge": str})   # código como texto, sempre

    # Tudo dentro de uma transação: ou a carga inteira dá certo, ou nada muda no banco.
    with engine.begin() as conn:
        conn.exec_driver_sql(SQL_CRIAR.read_text(encoding="utf-8"))
        conn.execute(text(f"TRUNCATE TABLE {TABELA}"))          # esvazia sem apagar a tabela
        tabela.to_sql(TABELA, conn, if_exists="append", index=False, method="multi")
    return len(tabela)


# [D] Conferência: lê de volta do banco e compara com o gabarito -----------------------
def conferir(engine, linhas_csv: int) -> None:
    with engine.connect() as conn:
        linhas_banco = conn.execute(text(f"SELECT COUNT(*) FROM {TABELA}")).scalar()
        sp = conn.execute(text(f"""
            SELECT 100.0 * SUM(nv_menos_7_consultas) / SUM(nv_consultas_informadas),
                   1000.0 * SUM(casos_sc) / SUM(nascidos_vivos)
            FROM {TABELA} WHERE ano = 2023""")).one()

    print(f"Linhas no CSV: {linhas_csv} · linhas no banco: {linhas_banco}")
    print(f"Conferência SP 2023 lida do banco: {sp[0]:.1f}% com menos de 7 consultas (gabarito 17,1%) · "
          f"{sp[1]:.1f} casos por mil NV (gabarito 8,5)")
    if linhas_banco != linhas_csv:
        sys.exit("ERRO: o banco não tem o mesmo número de linhas do CSV.")
    print("Carga OK.")


# [E] Execução ------------------------------------------------------------------------
if __name__ == "__main__":
    engine = conectar()
    n = carregar(engine)
    conferir(engine, n)
