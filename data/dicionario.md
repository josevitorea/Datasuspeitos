# Dicionário de dados · tabela final (município × ano)

Uma linha por **município do estado de SP × ano**, de 2019 a 2023.
645 municípios × 5 anos = **3.225 linhas**. Chave única: `cod_ibge` + `ano`.

A tabela guarda **contagens** (números de pessoas e de casos). Os percentuais e as taxas são calculados no Power BI,
somando numeradores e denominadores. Assim o indicador fica certo para um município, para uma região ou para o estado inteiro.

## Bases de origem

| Base | Arquivo | O que usamos |
|---|---|---|
| SINASC (nascidos vivos), via TabNet | `TabNet SINASC SP - consultas pre-natal por municipio - AAAA.csv` (um arquivo por ano) | Nascidos vivos por número de consultas de pré-natal |
| Painel de Indicadores de Sífilis (Ministério da Saúde) | `painelSifilis.xlsx` | Casos de sífilis congênita e momento do diagnóstico da sífilis da mãe |

## Colunas

| Coluna | Tipo | O que significa | De onde vem | Regra |
|---|---|---|---|---|
| `cod_ibge` | texto (6 caracteres) | Código do município no IBGE. É a "chave" que liga as duas bases | TabNet: 6 primeiros caracteres da coluna `Município` (ex.: `"350010 ADAMANTINA"` → `350010`). Painel: coluna `Código` | Sempre texto, nunca número. No pandas o `Código` do painel chega como decimal (`353440.0`) e precisa virar inteiro antes de virar texto. Só entram códigos de 6 dígitos que começam com `35` (SP): linhas de estado, região e Brasil têm código mais curto e são descartadas |
| `municipio` | texto | Nome do município | Painel: coluna `Nome Município` | Usamos o nome do painel porque vem com acentos (`Osasco`, `Aguaí`). O TabNet vem em maiúsculas e sem acento |
| `ano` | número inteiro | Ano do nascimento / da notificação | TabNet: um arquivo por ano (linha `Período` no topo). Painel: final do nome de cada coluna (`... 2019`, `... 2020` etc.) | Só 2019 a 2023. 2024 fica de fora (dados de sífilis incompletos) |
| `nascidos_vivos` | número inteiro | Total de bebês nascidos vivos de mães que moram no município | TabNet: coluna `Total` | No TabNet, zero aparece como `-` e vira `0`. Município que não aparece no TabNet teve zero nascimentos no ano e recebe `0` (ex.: Borá em 2023) |
| `nv_consultas_informadas` | número inteiro | Nascidos vivos em que o número de consultas de pré-natal foi registrado | TabNet: `Total` − `Ignorado` | É o denominador do % de pré-natal insuficiente. Quem tem consultas "ignoradas" não entra na conta |
| `nv_menos_7_consultas` | número inteiro | Nascidos vivos cuja mãe fez menos de 7 consultas de pré-natal | TabNet: `Nenhuma` + `De 1 a 3 consultas` + `De 4 a 6 consultas` | 7 consultas é o mínimo recomendado. Abaixo disso, consideramos o pré-natal insuficiente |
| `casos_sc` | número inteiro | Casos de sífilis congênita em menores de 1 ano | Painel, aba `DADOS CONTINUAÇÃO 2`, coluna `Sífilis congênita em menores de um ano AAAA` | Usar a coluna de **casos**. As colunas `Tx Det AAAA` são fórmulas do Excel e não são usadas |
| `casos_sc_diag_prenatal` | número inteiro | Desses casos, em quantos a sífilis da mãe foi diagnosticada **durante o pré-natal** | Painel, aba `DADOS CONTINUAÇÃO 4`, coluna `Durante o pré-natal AAAA` | Faz parte do "momento do diagnóstico" da mãe. Os 5 momentos (pré-natal, parto, após o parto, não realizado, ignorado) somam exatamente `casos_sc`. Conferido: SP 2023 = 2.837 de 4.276 (66,3%) |
| `elegivel_ranking` | verdadeiro/falso | Se o município entra no ranking e no quadrante | Calculada no script | Verdadeiro quando `nascidos_vivos` ≥ 1.000 no ano. Em municípios pequenos, 1 ou 2 casos fazem a taxa explodir e o ranking fica injusto |

## Indicadores (calculados no Power BI, não guardados na tabela)

**% com menos de 7 consultas** = `nv_menos_7_consultas` ÷ `nv_consultas_informadas` × 100
Fica de fora: nascimentos com consultas "Ignorado".

**Taxa de sífilis congênita por mil nascidos vivos** = `casos_sc` ÷ `nascidos_vivos` × 1.000
Município com zero nascidos vivos fica **em branco** (não dá para dividir por zero). Meta OPAS/OMS: menos de 0,5.

**% de casos com sífilis materna diagnosticada no pré-natal** = `casos_sc_diag_prenatal` ÷ `casos_sc` × 100
Município com zero casos fica **em branco**, não 0% nem 100%: sem casos, a pergunta não se aplica.
Em 2023, 319 dos 645 municípios tiveram zero casos.

## Conferências (gabarito, ano 2023)

| Recorte | % menos de 7 consultas | Sífilis congênita por mil NV | % diagnosticada no pré-natal |
|---|---|---|---|
| Estado de SP | 17,1% | 8,5 | 66,3% |
| Osasco | 29,3% | 33,6 | 78,5% (216 de 275) |

Pequenas diferenças na segunda casa decimal são esperadas: o painel de sífilis e o TabNet foram extraídos em datas diferentes
(nascidos vivos de 2023: 503.910 no TabNet × 503.879 no painel).
