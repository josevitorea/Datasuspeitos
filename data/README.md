# Dados do projeto · como baixar as bases

Os dados brutos **não ficam no GitHub**: a planilha de sífilis tem 36 MB. Este guia mostra como baixar cada base, do zero, para rodar o projeto em qualquer computador.

Depois de baixar, coloque **todos os arquivos na pasta `data/raw/`** do repositório, com os nomes exatamente como indicados abaixo. O script `src/tratamento.py` procura os arquivos por esses nomes.

| Base | O que traz | Quem publica | Arquivos |
|---|---|---|---|
| SINASC (Nascidos Vivos), via TabNet | Nascidos vivos por município e número de consultas de pré-natal | Ministério da Saúde / DATASUS | 5 arquivos `.csv`, um por ano (2019 a 2023) |
| Painel de Indicadores de Sífilis | Casos de sífilis congênita e momento do diagnóstico da mãe, por município e ano | Ministério da Saúde | 1 arquivo `.xlsx` |

---

## 1. Nascidos vivos e consultas de pré-natal (TabNet / SINASC)

1. Acesse o TabNet de Nascidos Vivos do estado de São Paulo:
   https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinasc/cnv/nvsp.def
2. Configure a tabela:
   - **Linha:** Município
   - **Coluna:** Consult pré-natal
   - **Conteúdo:** Nascim p/resid.mãe *(nascimentos contados pelo município onde a mãe mora)*
   - **Períodos disponíveis:** marque **um ano só**, começando por 2019. Desmarque qualquer outro ano que já venha selecionado.
   - **Seleções disponíveis:** não altere nada.
3. No formato, escolha **"Tabela com bordas"** e clique em **Mostra**.
4. No fim da página do resultado, clique no link para baixar a tabela em **CSV**.
5. Renomeie o arquivo baixado para:

   ```
   TabNet SINASC SP - consultas pre-natal por municipio - 2019.csv
   ```

6. Repita os passos 2 a 5 para **2020, 2021, 2022 e 2023**, trocando o ano no nome do arquivo.

**Como conferir se baixou certo:** abra o arquivo no Bloco de Notas. A 3ª linha deve mostrar o ano (`Período:2019`) e a 4ª linha deve ser o cabeçalho:
`"Município";"Nenhuma";"De 1 a 3 consultas";"De 4 a 6 consultas";"7 ou mais consultas";"Ignorado";"Total"`

**Cuidados:**
- O arquivo usa ponto e vírgula (`;`) como separador e acentuação antiga do Windows (latin-1). O script já trata isso. Não abra e salve no Excel, porque ele pode mudar o formato.
- Onde o valor é zero, o TabNet escreve um traço (`-`).
- Existe uma linha "MUNICIPIO IGNORADO - SP", sem código. O script descarta essa linha.
- Os dados até 2024 são finais. 2024 fica fora do nosso recorte porque os dados de sífilis daquele ano estão incompletos.

---

## 2. Sífilis congênita (Painel de Indicadores de Sífilis)

1. Acesse o Painel de Indicadores de Sífilis do Ministério da Saúde:
   https://indicadoressifilis.aids.gov.br/
2. No topo da página, clique em **"Planilha de todos os municípios"**.
   Link direto: https://indicadoressifilis.aids.gov.br/documentos/painelSifilis.xlsx
3. Salve o arquivo com o nome original:

   ```
   painelSifilis.xlsx
   ```

**O que usamos da planilha** (o resto não entra no projeto):
- Aba `DADOS CONTINUAÇÃO 2`, colunas `Sífilis congênita em menores de um ano 2019` a `2023`
- Aba `DADOS CONTINUAÇÃO 4`, colunas `Durante o pré-natal 2019` a `2023`

**Cuidados:**
- A planilha traz o Brasil inteiro, com linhas de total (estado, região, país) misturadas às de município. O script fica só com os municípios de SP (código de 6 dígitos começando com 35).
- As colunas de taxa (`Tx Det`) são fórmulas do Excel. Não as usamos: as taxas são calculadas no Power BI.
- Os dados de 2024 vão só até 30/06/2024, por isso ficam fora do recorte.
- O Ministério atualiza a planilha periodicamente, então os números podem mudar um pouco conforme a data do download.

---

## 3. Depois de baixar

A pasta `data/raw/` deve ficar assim:

```
data/raw/
├── TabNet SINASC SP - consultas pre-natal por municipio - 2019.csv
├── TabNet SINASC SP - consultas pre-natal por municipio - 2020.csv
├── TabNet SINASC SP - consultas pre-natal por municipio - 2021.csv
├── TabNet SINASC SP - consultas pre-natal por municipio - 2022.csv
├── TabNet SINASC SP - consultas pre-natal por municipio - 2023.csv
└── painelSifilis.xlsx
```

Para gerar a tabela final, rode na pasta raiz do repositório:

```
python src/tratamento.py
```

O significado de cada coluna da tabela final está em [`dicionario.md`](dicionario.md).
