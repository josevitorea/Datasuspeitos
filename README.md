<div align="center">

# Saúde da Gestante em Dados: pré-natal e sífilis congênita nos municípios de SP

**Onde o pré-natal falha e a sífilis congênita avança nos municípios de São Paulo**

![ODS 3](https://img.shields.io/badge/ODS_3-Sa%C3%BAde_e_Bem--Estar-4C9F38?style=for-the-badge)
![FMU Tech Inovação](https://img.shields.io/badge/FMU_Tech_Inova%C3%A7%C3%A3o-2026.2-4B1D72?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Checkpoint_2-8B3FD9?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Dados abertos](https://img.shields.io/badge/Dados-DATASUS-0B5394?style=flat-square)


 <img src="docs/identidade/logo.png" alt="Logo do projeto" width="220"> 

</div>

---

> **Cada caso de sífilis congênita é um pré-natal que não funcionou.**
> Este projeto cruza dados públicos de pré-natal e de sífilis congênita para mostrar, município a município no estado de São Paulo, onde o cuidado à gestante está falhando e onde agir primeiro.

| | |
|---|---|
| **Grupo** | DataSUSpeitos |
| **Desafio** | FMU Tech Inovação 2026.2 · ODS 3 — Saúde e Bem-Estar |
| **Recorte** | Municípios do estado de São Paulo, de 2019 a 2023 |
| **Mentor** | Prof. Gerson Lourenço Gazola |
| **Etapa atual** | Checkpoint 2 — Protótipo |

## Sumário

1. [Integrantes](#integrantes)
2. [O problema](#o-problema)
3. [Público e contexto](#público-e-contexto)
4. [Bases de dados](#bases-de-dados)
5. [Proposta de solução](#proposta-de-solução)
6. [Requisitos](#requisitos)
7. [Protótipo](#protótipo)
8. [Principais achados](#principais-achados)
9. [Como executar](#como-executar)
10. [Tecnologias e justificativa](#tecnologias-e-justificativa)
11. [Identidade visual](#identidade-visual)
12. [Pitch](#pitch)
13. [Orientação do mentor](#orientação-do-mentor)
14. [Evolução desde o Checkpoint 1](#evolução-desde-o-checkpoint-1)
15. [Uso de IA no projeto](#uso-de-ia-no-projeto)
16. [Estrutura do repositório](#estrutura-do-repositório)
17. [Andamento do projeto](#andamento-do-projeto)

---

## Integrantes

| Nome | Papel no projeto | GitHub |
|---|---|---|
| Kaike Martins | Organização do grupo, tratamento dos dados, banco de dados e análise | [@kaike-martins](https://github.com/kaike-martins) |
| Raquel Costa Pereira | Problema, contexto, pitch, requisitos, evolução, vídeo e contato com o mentor | [@rachelpereira8663](https://github.com/rachelpereira8663) |
| Vitória da Silva | Identidade visual, tema do painel, guia de download das bases e prints | [@vitoria1551](https://github.com/vitoria1551) |
| José Vitor Gonçalves | Repositório, tecnologias e painel em Power BI | [@josevitorea](https://github.com/josevitorea) |

---

## O problema

No estado de São Paulo, entre 2019 e 2023, o acompanhamento gestacional inadequado está associado à incidência de infecções congênitas, evidenciando que cada caso de sífilis congênita representa um atendimento de pré-natal que não se completou de forma efetiva.

O público afetado engloba gestantes e recém-nascidos em todo o território paulista, com cenários particularmente críticos em municípios da Região Metropolitana, como Osasco e Carapicuíba, onde tanto a taxa de sífilis congênita quanto o percentual de gestantes com menos de 7 consultas estão muito acima da média estadual.

Em 2023, o estado registrou 4.276 bebês nascidos com sífilis congênita (Painel de Indicadores de Sífilis, Ministério da Saúde), o que representa uma taxa de 8,5 casos a cada 1.000 nascidos vivos, muito acima da meta de eliminação da OPAS/OMS, fixada em 0,5 por 1.000 nascidos vivos. No mesmo período, 82,7% das mães desses bebês realizaram consultas de pré-natal e 66,3% tiveram o diagnóstico da doença identificado durante o acompanhamento. Além disso, dados do SINASC indicam que 17,1% dos bebês nascidos no estado (86.190 crianças em um total de 503.910 nascidos vivos) vieram de mães que realizaram menos de 7 consultas de pré-natal.

Essa realidade importa porque o agravo é evitável: o diagnóstico é simples e acessível na rotina de acompanhamento, e o tratamento possui baixo custo e alta eficácia no âmbito do SUS. A falha observada não recai sobre as gestantes, mas sim sobre o sistema de cuidado, que não assegura a integralidade do tratamento e o vínculo contínuo. Dessa forma, o projeto conecta-se diretamente às metas 3.1, 3.2 e 3.3 do ODS 3 da Agenda 2030.

## Público e contexto

O problema afeta diretamente gestantes e recém-nascidos, sobretudo em municípios onde a cobertura e a retenção no pré-natal apresentam maiores fragilidades. A solução desenvolvida destina-se a gestores municipais de saúde e equipes da atenção básica (unidades básicas de saúde), que poderão utilizá-la como ferramenta estratégica para identificar quais municípios prioritários demandam ações imediatas de busca ativa de gestantes, ampliação da testagem e garantia do tratamento completo.

---

## Bases de dados

| Base | Fonte | O que usamos | Nível | Período |
|---|---|---|---|---|
| SINASC — Nascidos Vivos | [TabNet / DATASUS](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinasc/cnv/nvsp.def) | Nascidos vivos e número de consultas de pré-natal da mãe | Município de residência da mãe | 2019–2023 |
| Painel de Indicadores de Sífilis | [Ministério da Saúde](https://indicadoressifilis.aids.gov.br/) | Casos de sífilis congênita e momento do diagnóstico da sífilis da mãe | Município de residência | 2019–2023 |

As duas bases são unidas pelo **código IBGE do município (6 dígitos)**, formando uma tabela com uma linha por município e ano: **645 municípios × 5 anos = 3.225 linhas**.

- **Como baixar as bases:** passo a passo em [`data/README.md`](data/README.md)
- **O que significa cada coluna da tabela final:** [`data/dicionario.md`](data/dicionario.md)

**Limitações conhecidas:**

- **Municípios pequenos têm taxas instáveis.** Em uma cidade com 200 nascimentos, um único caso de sífilis congênita já gera uma taxa de 5 por mil, o que pode colocá-la no topo do ranking por acaso. Por isso, o ranking considera apenas municípios com pelo menos 1.000 nascidos vivos no ano.
- **Subnotificação.** Um município que testa e notifica pouco aparece com menos casos do que tem na realidade, então uma taxa baixa pode ser falsa. Como pouco pré-natal costuma significar pouca testagem, o painel destaca municípios com pré-natal ruim e sífilis baixa como casos a investigar.
- **Período de 2019 a 2023.** O Painel de Sífilis traz os casos de 2024 só até 30/06/2024. Incluir 2024 compararia meio ano de casos com um ano inteiro de nascimentos e mostraria uma queda falsa da sífilis congênita.
- **Os dados mostram municípios, não pessoas.** As informações de pré-natal e de sífilis estão agregadas por município, em bases separadas, então não é possível ligar cada bebê com sífilis às consultas que a mãe fez. O painel mostra que pré-natal insuficiente e sífilis alta aparecem juntos em um município, mas não prova que as mães com menos consultas são as mesmas dos bebês com sífilis. Por isso, ele serve para priorizar municípios onde agir, e não para explicar a causa de cada caso.
- **Informação ignorada.** No SINASC, parte das declarações não informa o número de consultas (868 em 2023, no estado). Esses registros são excluídos do cálculo do percentual de pré-natal insuficiente.
- **Mudanças de notificação.** Saltos bruscos de um ano para outro em um município (como em Osasco, de 2021 para 2022) podem refletir melhora na investigação e no registro de casos, e não só piora real. Esses saltos devem ser lidos com cautela.

---

## Proposta de solução

O projeto entrega um painel que mostra, para cada município do estado de São Paulo, onde o pré-natal está falhando e onde essa falha já resulta em bebês nascidos com sífilis.

O público-alvo são os gestores municipais de saúde e as equipes da atenção básica, que podem usar o painel para decidir em quais municípios priorizar a busca ativa de gestantes, a testagem e o tratamento.

O painel mostra três camadas para cada município:

| Camada | Indicador | Cálculo |
|---|---|---|
| **Acesso** | % de mães com menos de 7 consultas de pré-natal | (Nenhuma + 1 a 3 + 4 a 6 consultas) ÷ (Total − Ignorado) × 100 |
| **Consequência** | Taxa de sífilis congênita | Casos ÷ nascidos vivos × 1.000 |
| **Qualidade do cuidado** | % de casos com a sífilis da mãe diagnosticada durante o pré-natal | Casos com diagnóstico no pré-natal ÷ casos × 100 |

Medir as três é necessário porque, em 2023, 82,7% dos bebês com sífilis no estado tinham mães que fizeram pré-natal: o problema não é só chegar ao serviço, é o cuidado se completar.

**Municípios prioritários** são aqueles com, ao mesmo tempo, percentual de pré-natal insuficiente **e** taxa de sífilis congênita acima da média do estado no ano.

### Como os dados chegam ao painel

```text
Dados públicos            Tratamento (Python)           Banco de dados             Painel
TabNet (5 CSVs)    →   src/tratamento.py         →   PostgreSQL            →   Power BI
Painel de Sífilis      limpa, une pelo código        tabela                    visão geral, quadrante,
(planilha .xlsx)       IBGE e confere os números     fato_municipio_ano        ranking e detalhe
                       contra um gabarito            (src/carga_postgres.py)   do município
```

A qualidade dos dados é conferida duas vezes: o script de tratamento para se encontrar linha repetida, município faltando, contagem impossível ou número do estado diferente do gabarito, e o próprio banco recusa dados incoerentes por meio de regras na tabela (`sql/criar_tabela.sql`).

---

## Requisitos

Os requisitos completos, funcionais e não funcionais, estão em [`docs/requisitos.md`](docs/requisitos.md). Os essenciais para este checkpoint são:

- **RF01** · Ver, para o estado de São Paulo e o ano escolhido, os 4 números principais: nascidos vivos, % de mães com menos de 7 consultas de pré-natal, taxa de sífilis congênita por mil nascidos vivos e % de casos em que a sífilis da mãe foi diagnosticada durante o pré-natal.
- **RF02** · Acompanhar a evolução dos indicadores do estado de 2019 a 2023
- **RF03** · Ver, num quadrante, quais municípios têm ao mesmo tempo pré-natal pior e sífilis congênita maior que a média do estado. Esses municípios aparecem destacados como prioritários.
- **RF04** · Ver o ranking dos municípios, do mais crítico para o menos crítico, com os três indicadores lado a lado.
- **RF05** · Escolher um município e ver os três indicadores dele de 2019 a 2023, comparados com a média do estado.
- **RF06** · Filtrar todas as páginas por ano.

---

## Protótipo

O protótipo é um painel em Power BI com 4 páginas, alimentado pelos dados reais dos 645 municípios do estado:

| Página | O que mostra |
|---|---|
| **Visão geral** | Os 4 números principais do estado no ano escolhido e a evolução de 2019 a 2023 |
| **Quadrante** | Cada município como um ponto: pré-natal insuficiente × taxa de sífilis congênita, com linhas na média do estado. Os prioritários aparecem destacados |
| **Ranking** | Os municípios do mais crítico para o menos crítico, com os três indicadores lado a lado |
| **Detalhe do município** | Os três indicadores de um município de 2019 a 2023, comparados com a média do estado |

### Prints

*(em construção)*

### Vídeo de demonstração

[![Assista ao vídeo de demonstração no YouTube](https://img.youtube.com/vi/UtmDvxhS1Dw/hqdefault.jpg)](https://youtu.be/UtmDvxhS1Dw)

▶️ **[Assistir no YouTube](https://youtu.be/UtmDvxhS1Dw)** · 2min23s · narração de Raquel Costa Pereira

O vídeo é uma animação feita com os dados reais do projeto: mostra o pipeline rodando (tratamento, conferência e carga no banco) e o fluxo principal pelas 4 páginas do painel. Os números exibidos vêm da tabela final do projeto (`data/processed/tabela_final.csv`).

---

## Principais achados

**1. O pré-natal melhorou, mas a sífilis congênita piorou.** Entre 2019 e 2023, a parcela de bebês cujas mães fizeram menos de 7 consultas caiu de 19,5% para 17,1% no estado. No mesmo período, a taxa de sífilis congênita subiu de 6,8 para 8,5 casos por mil nascidos vivos.

| Ano | % com menos de 7 consultas | Sífilis congênita por mil NV | % de casos com diagnóstico no pré-natal |
|---|---|---|---|
| 2019 | 19,5% | 6,8 | 62,4% |
| 2020 | 19,1% | 6,7 | 62,1% |
| 2021 | 18,1% | 7,6 | 65,1% |
| 2022 | 18,6% | 8,9 | 66,7% |
| 2023 | 17,1% | 8,5 | 66,3% |

**2. O diagnóstico acontece, mas não vira proteção para o bebê.** A parcela de casos em que a sífilis da mãe foi diagnosticada durante o pré-natal subiu de 62% para 66%. Ou seja: em 2 de cada 3 bebês que nasceram com sífilis em 2023, a doença da mãe já era conhecida antes do parto. O gargalo provável está no que acontece depois do diagnóstico, no tratamento, e não só no acesso ao pré-natal. Em Osasco, isso chega a 78,5% dos casos (216 de 275).

**3. O problema está concentrado, e em boa parte é antigo.** Em 2023, os 27 municípios prioritários somaram 18,9% dos nascidos vivos do estado, mas 36,7% dos casos de sífilis congênita (1.571 de 4.276). Ou seja, quase o dobro do que o tamanho deles explicaria. E 11 municípios foram prioritários em todos os 5 anos analisados: Carapicuíba, Cubatão, Embu das Artes, Ferraz de Vasconcelos, Guarujá, Guarulhos, Itaquaquecetuba, Mauá, Osasco, São Vicente e Taubaté. Para o gestor, isso indica onde começar: uma ação focada em poucos municípios alcança mais de um terço dos casos do estado.

> Estes achados descrevem municípios e o estado, não pessoas (ver limitações em [Bases de dados](#bases-de-dados)).

---

## Como executar

Há dois caminhos, dependendo do que você quer fazer.

### Caminho A · Só ver o painel *(em construção)*

### Caminho B · Rodar o pipeline completo (dados → banco → painel)

**Pré-requisitos:** [Python 3](https://www.python.org/downloads/), [PostgreSQL](https://www.postgresql.org/download/) e, para olhar o banco, [DBeaver](https://dbeaver.io/) (opcional).

1. **Baixe o repositório** (Code → Download ZIP) e abra um terminal na pasta principal dele.
2. **Instale as bibliotecas do Python:**
   ```
   pip install -r requirements.txt
   ```
3. **Crie o banco de dados** no PostgreSQL (pelo DBeaver ou pelo terminal do PostgreSQL):
   ```sql
   CREATE DATABASE datasuspeitos;
   ```
4. **Configure o acesso ao banco:** copie o arquivo `.env.example` para um novo arquivo chamado `.env` e preencha com o usuário e a senha do seu PostgreSQL. O `.env` nunca vai para o GitHub.
5. **Carregue a tabela no banco:**
   ```
   python src/carga_postgres.py
   ```
   O script cria a tabela `fato_municipio_ano`, carrega as 3.225 linhas de `data/processed/tabela_final.csv` e confere o resultado. O esperado é terminar com `Carga OK.`
6. **Abra o painel no Power BI** *(em construção)*

**Opcional · refazer o tratamento a partir das bases originais:** baixe as bases seguindo [`data/README.md`](data/README.md), coloque os arquivos em `data/raw/` e rode, antes do passo 5:
```
python src/tratamento.py
```
O script gera de novo a `data/processed/tabela_final.csv` e termina com `Verificações OK`.

> No Windows, se o terminal disser que `python` não é reconhecido, use `py` no lugar (por exemplo, `py src/carga_postgres.py`).

---

## Tecnologias e justificativa

| Tecnologia | Para que serve no projeto | Por que ela, no nosso caso | Alternativa descartada |
|---|---|---|---|
| **Python (pandas)** | Ler, limpar, unir e conferir as duas bases | Os arquivos do TabNet vêm com acentuação antiga (latin-1), cabeçalho e rodapé de texto, traço (`-`) no lugar de zero e um ano em cada arquivo. A planilha de sífilis tem 36 MB, traz o Brasil inteiro e mistura linhas de total com linhas de município. Com pandas, tudo isso vira código que roda igual toda vez e confere o resultado contra um gabarito, em vez de ser feito à mão no Excel | Excel / Power Query: o tratamento ficaria em cliques difíceis de revisar e repetir, e a planilha de 36 MB fica lenta |
| **PostgreSQL** | Guardar a tabela final (município × ano) | A tabela tem regras que o próprio banco garante: cada município aparece uma vez por ano (chave primária) e nenhum valor impossível entra, como casos negativos ou mais casos diagnosticados que casos totais (regras `CHECK`). É gratuito e roda localmente, então qualquer pessoa reproduz o projeto | Servidor de banco da faculdade: só funciona dentro da rede da FMU |
| **Power BI** | Painel com visão geral, quadrante, ranking e detalhe | O público é o gestor de saúde, que precisa filtrar por ano e por município sem saber programar. As porcentagens e taxas são calculadas em DAX somando numerador e denominador, o que evita o erro de tirar média de porcentagens | Gráficos fixos em Python: não deixam o gestor explorar os dados sozinho |
| **DBeaver** | Ver e consultar o banco | Gratuito, funciona com PostgreSQL e é o programa usado nas aulas de banco de dados. Usamos para conferir a carga com consultas SQL | pgAdmin |
| **GitHub** | Versionar e entregar o projeto | A entrega é pelo link do repositório. O código, a documentação e o histórico de mudanças ficam públicos, e os dados brutos ficam de fora (são grandes e qualquer um baixa da fonte oficial) | — |

---

## Identidade visual

<p align="center"><img src="docs/identidade/logo.png" alt="Logo do projeto" width="200"></p>

**Logo:** um pino de mapa com um embrião e um gráfico de barras. O pino de mapa representa a localização, pois a análise é feita por município. O embrião representa o bebê em desenvolvimento durante a gestação. O gráfico de barras representa a análise estatística e a apresentação dos dados em um painel.

### Paleta de cores

| Cor | HEX | Uso |
|---|---|---|
| Principal | #174A5B | Títulos e elementos principais |
| Secundária | #70A6A8 | Barras e pontos dos demais municípios |
| Apoio | #7950A1 | Linhas de referência, como a média do estado |
| **Destaque** | #C8572B | **Somente municípios prioritários** |
| Fundo | #F7F4EF | Fundo do painel e dos slides |
| Neutro | #E9DCCB | Bordas e divisórias |

A cor de destaque é usada só para os municípios prioritários, para que o gestor os encontre de imediato. Ela foi testada para continuar visível para pessoas com daltonismo.

**No painel:** a paleta é aplicada pelo tema [`docs/identidade/tema-datasuspeitos.json`](docs/identidade/tema-datasuspeitos.json). A cor de destaque fica fora do tema de propósito, para aparecer só nos municípios prioritários.

**Tipografia:** Montserrat nos títulos e Open Sans nos textos (Google Fonts). No painel do Power BI, usamos Segoe UI, fonte padrão do programa, para garantir que o texto apareça igual em qualquer computador.

## Pitch

Em 2023, 8,5 a cada 1.000 bebês nasceram com sífilis congênita no estado de São Paulo. E 82,7% das mães desses bebês fizeram pré-natal: estavam no serviço, mas o cuidado não se completou. Para enfrentar esse desafio, o grupo DataSUSpeitos está desenvolvendo um painel analítico interativo que cruza dados de pré-natal e de sífilis congênita por município. O nosso diferencial é integrar essas bases públicas em uma única interface intuitiva, apontando em quais municípios os gestores públicos devem agir primeiro.

## Orientação do mentor

Conversa com o Prof. Gerson em 07/10/2026:

| Dúvida | Orientação |
|---|---|
| Como é a entrega? | Pelo link do repositório no portal Level Up |
| Power BI conta como protótipo? | Sim. Uso de machine learning seria um diferencial |
| Pode usar IA? | Sim, desde que o uso seja documentado no repositório |
| Recorte | Livre. O grupo escolheu municípios de SP, de 2019 a 2023 |
| Banco de dados | Pode ser usado |

Em 03/11/2026, o Prof. Gerson elogiou a primeira parte do trabalho e orientou o grupo a seguir pelo mesmo caminho (ver [Evolução desde o Checkpoint 1](#evolução-desde-o-checkpoint-1)).

---

## Evolução desde o Checkpoint 1

No Checkpoint 1 apresentamos a ideia e o desenho da solução. No Checkpoint 2, a arquitetura proposta foi construída e está funcionando com dados reais.

| Tema | No CP1 | No CP2 | Por que mudou |
|---|---|---|---|
| Protótipo | Painel descrito no README, sem dados | Painel em Power BI com 4 páginas, alimentado por dados reais | Objetivo do CP2: protótipo funcional, com o fluxo principal navegável |
| Dados | Números-chave de 2023 conferidos manualmente | Tabela final com os 645 municípios de SP, de 2019 a 2023 (3.225 linhas), gerada por script | Recorte aprovado pelo mentor: municípios de SP, 2019 a 2023 |
| Tratamento | Previsto | Script `src/tratamento.py`, que une as bases pelo código IBGE e confere os resultados contra um gabarito | Garantir que todo número do painel tem origem rastreável e verificada |
| Banco de dados | "Banco da disciplina" | PostgreSQL instalado localmente, com script SQL versionado | O servidor da faculdade só funciona na rede da FMU; com o banco local, qualquer pessoa reproduz o projeto |
| Documentação | README com problema, solução, bases e identidade visual | + dicionário de dados, guia de download das bases, requisitos e instruções de execução | Permitir que outra pessoa rode o projeto sem ajuda |
| Requisitos | Não existiam | [`docs/requisitos.md`](docs/requisitos.md) | Exigência do edital para o 2º semestre |
| Tecnologias | Justificativas genéricas | Justificativas reescritas a partir dos problemas reais que encontramos nos dados | Mostrar por que cada ferramenta resolve um problema do nosso projeto |
| Planejamento | Tarefas do protótipo pensadas como um aplicativo | Tarefas revisadas para o que o protótipo é: painel + pipeline de dados | Coerência entre o plano e a solução proposta no CP1 |

### Retorno do mentor ao longo do CP2

| Data | O que o Prof. Gerson disse | O que o grupo fez |
|---|---|---|
| 07/10/2026 | Power BI conta como protótipo; machine learning seria um diferencial; IA pode ser usada, desde que documentada no repositório; banco de dados pode ser usado; o recorte é livre; a entrega é pelo link do repositório. | Mantivemos Power BI + PostgreSQL, registramos o uso de IA no README, entregamos pelo repositório e ficamos com SP, de 2019 a 2023. O agrupamento por machine learning ficou como ideia para depois do CP2. |
| 03/11/2026 | Elogiou a primeira parte do trabalho e orientou o grupo a seguir pelo mesmo caminho. | Mantivemos o planejamento e seguimos com a construção do pipeline de dados e do painel. |

---

## Uso de IA no projeto

Seguindo a orientação do mentor, documentamos aqui como a inteligência artificial foi usada. A IA foi uma ferramenta de apoio; **as decisões do projeto são do grupo**, e cada integrante revisou e é responsável pelo que subiu com o próprio nome.

**Ferramentas:** Claude (Anthropic), usado principalmente pelo organizador do grupo; Gemini (Google), usado por integrantes para revisar a redação dos textos e gerar o logo.

### Checkpoint 1

| Etapa | Como a IA ajudou | O que foi decidido ou feito pelo grupo |
|---|---|---|
| Planejamento | Sugestão de cronograma, quadro de tarefas e divisão inicial de papéis | Papéis e prazos confirmados e ajustados pelo grupo |
| Escolha do tema | Levantamento de 6 temas do ODS 3 com bases públicas verificadas | Tema escolhido por votação unânime, unindo duas das sugestões |
| Pesquisa e dados | Busca de fontes oficiais e conferência dos arquivos baixados, como a identificação de linhas de total que duplicavam somas e do corte nos dados de 2024 | Recorte (municípios de SP, 2019 a 2023) definido pelo grupo e aprovado pelo mentor |
| Textos | Revisão crítica dos rascunhos e sugestão de versões corrigidas | Cada seção partiu de um rascunho do seu responsável, que decidiu o que manter |
| Identidade visual | Geração do logo e de opções de paleta; teste de contraste e daltonismo | Escolha da paleta, inclusão da cor de destaque e conceito do logo |

### Checkpoint 2

| Etapa | Como a IA ajudou | O que foi decidido ou feito pelo grupo |
|---|---|---|
| Dados e código | Escrita do dicionário de dados e dos scripts de tratamento, de carga no banco e de criação da tabela | O organizador baixou as bases, instalou e configurou o PostgreSQL, rodou o pipeline e conferiu os resultados contra o gabarito e com consultas SQL próprias |
| Documentação | Rascunho do guia de download das bases, dos requisitos e da seção de evolução | A Vitória testou o guia seguindo o texto e apontou três pontos confusos, que foram corrigidos; a Raquel revisou e ajustou requisitos e evolução |
| Tema do painel | Explicação dos campos do tema do Power BI e teste de contraste das cores | A Vitória escolheu as cores e corrigiu a escolha que tinha contraste baixo |
| Análise | Cálculo e conferência dos indicadores dos 5 anos | Interpretação dos achados e das limitações discutida pelo grupo |
| Vídeo de demonstração | Animação feita com os dados reais do projeto e sincronização com a narração | A Raquel escreveu e gravou a narração; o grupo escolheu usar a animação |
| README final | Integração das partes de cada integrante e revisão do texto | O organizador revisou e publicou a versão final |

**Princípios que seguimos:**

- Nenhum número entra no projeto sem que a fonte original seja conferida.
- Todo código foi executado e verificado contra números conferidos à mão antes de entrar no repositório.
- No Checkpoint 2, por causa do prazo, parte dos rascunhos foi gerada com IA. Cada um foi revisado por quem subiu o arquivo, e isso está registrado nesta tabela.
- Cada integrante precisa saber explicar a própria parte sem ajuda.

---

## Estrutura do repositório

```text
Datasuspeitos/
├── README.md                   → apresentação do projeto (esta página)
├── requirements.txt            → bibliotecas Python do projeto
├── .env.example                → modelo do acesso ao banco (sem senha)
├── data/
│   ├── README.md               → como baixar as bases
│   ├── dicionario.md           → o que significa cada coluna
│   ├── processed/
│   │   └── tabela_final.csv    → tabela final: 645 municípios × 2019–2023
│   └── raw/                    → bases originais (não vão para o GitHub)
├── src/
│   ├── tratamento.py           → lê, limpa, une e confere as bases
│   └── carga_postgres.py       → carrega a tabela final no PostgreSQL
├── sql/
│   └── criar_tabela.sql        → cria a tabela e as regras de qualidade no banco
├── dashboard/                  → arquivo do painel em Power BI (.pbix) (em construção)
└── docs/
    ├── requisitos.md           → requisitos da solução
    ├── identidade/             → logo e tema de cores do Power BI
    └── prints/                 → capturas do protótipo (em construção)
```

---

## Andamento do projeto

**Checkpoint 1 - Ideação** (entregue em 23/10/2026)

- [x] Repositório público criado
- [x] Tema e recorte definidos
- [x] Título do projeto
- [x] Descrição do problema, público e contexto
- [x] Bases de dados públicas identificadas
- [ ] Tecnologias com justificativa *(tabela entregue com justificativas genéricas; reescrita no CP2)*
- [x] Logo, paleta de cores e tipografia
- [x] Pitch inicial
- [x] Todos os integrantes identificados

**Checkpoint 2 - Protótipo** (entrega em 27/11/2026)

- [ ] Protótipo funcional com o fluxo principal navegável *(em construção)*
- [x] Código no repositório público do GitHub
- [x] README com detalhes do projeto
- [ ] README com instruções de "como executar" testadas *(em construção: pipeline completo já rodado do zero em computador do grupo; falta testar a abertura do painel)*
- [ ] Prints do protótipo no repositório *(em construção)*
- [x] Tecnologias utilizadas documentadas
- [x] Vídeo de demonstração do funcionamento
- [x] Evolução em relação ao Checkpoint 1 registrada

**Próxima etapa:** Banca final (07 e 08/12/2026)
