<div align="center">

# Saúde da Gestante em Dados: pré-natal e sífilis congênita nos municípios de SP

**Onde o pré-natal falha e a sífilis congênita avança nos municípios de São Paulo**

![ODS 3](https://img.shields.io/badge/ODS_3-Sa%C3%BAde_e_Bem--Estar-4C9F38?style=for-the-badge)
![FMU Tech Inovação](https://img.shields.io/badge/FMU_Tech_Inova%C3%A7%C3%A3o-2026.2-4B1D72?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Checkpoint_1-8B3FD9?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Dados abertos](https://img.shields.io/badge/Dados-DATASUS-0B5394?style=flat-square)

<!-- Vitória: quando o logo estiver pronto, suba em docs/identidade/logo.png e descomente a linha abaixo -->
<!-- <img src="docs/identidade/logo.png" alt="Logo do projeto" width="220"> -->

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
| **Etapa atual** | Checkpoint 1 — Ideação |

## Sumário

1. [Integrantes](#integrantes)
2. [O problema](#o-problema)
3. [Público e contexto](#público-e-contexto)
4. [Bases de dados](#bases-de-dados)
5. [Proposta de solução](#proposta-de-solução)
6. [Tecnologias e justificativa](#tecnologias-e-justificativa)
7. [Identidade visual](#identidade-visual)
8. [Pitch](#pitch)
9. [Orientação do mentor](#orientação-do-mentor)
10. [Uso de IA no projeto](#uso-de-ia-no-projeto)
11. [Estrutura do repositório](#estrutura-do-repositório)
12. [Andamento do projeto](#andamento-do-projeto)

---

## Integrantes

| Nome | Papel no projeto | GitHub |
|---|---|---|
| Kaike Martins | Organização, tratamento dos dados e arquitetura | [@kaike-martins](https://github.com/kaike-martins) |
| Raquel Costa Pereira | Problema, contexto, pitch e contato com o mentor | [@rachelpereira8663](https://github.com/rachelpereira8663) |
| Vitória da Silva | Bases de dados e identidade visual | [@vitoria1551](https://github.com/vitoria1551) |
| José Vitor Gonçalves | Tecnologias, requisitos e protótipo | [@josevitorea](https://github.com/josevitorea) |

---

## O problema

<!-- RAQUEL: responda em parágrafos curtos
     O quê? Pré-natal insuficiente e a sífilis congênita como consequência
     Onde? Municípios do estado de SP, 2019 a 2023
     Quem? Gestantes e bebês (perfil vem dos números da Vitória)
     Quanto? Pelo menos 2 números reais, com fonte
     Por que importa? Evitável; metas 3.1, 3.2 e 3.3 do ODS 3
     200 a 350 palavras. Apague este comentário quando escrever. -->

*Em construção.*

## Público e contexto

<!-- RAQUEL: quem é afetado pelo problema e quem vai usar a solução
     (gestores e equipes da atenção básica). Apague este comentário quando escrever. -->

*Em construção.*

---

## Bases de dados

<!-- VITÓRIA: preencha a tabela e escreva as limitações.
     Apague este comentário quando escrever. -->

| Base | Fonte | O que usamos | Período |
|---|---|---|---|
| SINASC — Nascidos Vivos | [TabNet / DATASUS](https://datasus.saude.gov.br/informacoes-de-saude-tabnet/) | Consultas de pré-natal por município | 2019–2023 |
| Painel de Indicadores de Sífilis | [Ministério da Saúde](https://indicadoressifilis.aids.gov.br/) | Sífilis congênita, pré-natal e tratamento das mães | 2019–2023 |

**Limitações conhecidas:**

- *Em construção.*

---

## Proposta de solução

O projeto propõe um painel que mostra, para cada município do estado de São Paulo, onde o pré-natal está falhando e onde essa falha já resulta em bebês nascidos com sífilis.

O público-alvo são os gestores municipais de saúde e as equipes da atenção básica, que podem usar o painel para decidir em quais municípios priorizar a busca ativa de gestantes, a testagem e o tratamento.

As fontes utilizadas são o SINASC, com o número de consultas de pré-natal de cada nascimento e o Painel de Indicadores de Sífilis do Ministério da Saúde, com os casos de sífilis congênita e as informações de pré-natal e tratamento das mães.

Os dados das duas fontes são tratados em Python, unidos pelo código de cada município e guardados em um banco de dados. O painel, feito em Power BI, mostra três camadas para cada município: o acesso ao pré-natal (gestantes com menos de 7 consultas), a consequência (taxa de sífilis congênita) e a qualidade do cuidado (mães diagnosticadas e tratadas adequadamente). Medir as três é necessário porque, em 2023, 82,7% dos bebês com sífilis no estado tinham mães que fizeram pré-natal: o problema não é só chegar ao serviço é o cuidado se completar.

O diferencial está no ranking dos municípios pelas maiores taxas de sífilis congênita (casos por mil nascidos vivos), cruzando dois indicadores: os municípios prioritários são aqueles com pré-natal ruim e sífilis alta ao mesmo tempo.

```text
Dados públicos  →  Python (tratamento)  →  Banco de dados  →  Power BI (painel)
(TabNet + Painel        limpeza e            tabelas por        quadrante e ranking
 de Sífilis)          cruzamento por         município e ano     de municípios
                      código do município
```

---

## Tecnologias e justificativa

<!-- VITOR: uma linha por tecnologia. Apague este comentário quando escrever. -->

| Tecnologia | Para que serve no projeto | Por que ela | Alternativa descartada |
|---|---|---|---|
| | | | |

---

## Identidade visual

<!-- VITÓRIA: logo, paleta e tipografia. Apague este comentário quando escrever. -->

**Paleta de cores**

| Cor | HEX | Uso |
|---|---|---|
| | | |

**Tipografia:** *em construção.*

---

## Pitch

<!-- RAQUEL: 80 a 120 palavras. Dor com número → quem sofre → o que fazemos → diferencial.
     Apague este comentário quando escrever. -->

*Em construção.*

---

## Orientação do mentor

<!-- RAQUEL: confira se o texto está igual ao que o professor disse. -->

Conversa com o Prof. Gerson em 07/10/2026:

| Dúvida | Orientação |
|---|---|
| Como é a entrega? | Pelo link do repositório no portal Level Up |
| Power BI conta como protótipo? | Sim. Uso de machine learning seria um diferencial |
| Pode usar IA? | Sim, desde que o uso seja documentado no repositório |
| Recorte | Livre. O grupo escolheu municípios de SP, de 2019 a 2023 |
| Banco de dados | Pode ser usado |

---

## Uso de IA no projeto


Seguindo a orientação do mentor, documentamos aqui como a inteligência artificial
foi usada. A IA foi uma ferramenta de apoio; **as decisões e os textos de cada
seção são do grupo**.

**Ferramenta:** Claude (Anthropic), usado principalmente pelo organizador do grupo.

| Etapa | Como a IA ajudou | O que foi decidido ou feito pelo grupo |
|---|---|---|
| Planejamento | Sugestão de cronograma, quadro de tarefas e divisão inicial de papéis | Papéis e prazos confirmados e ajustados pelo grupo |
| Escolha do tema | Levantamento de 6 temas do ODS 3 com bases públicas verificadas | Tema escolhido por votação unânime, unindo duas das sugestões |
| Pesquisa e dados | Busca de fontes oficiais e conferência dos arquivos baixados, como a identificação de linhas de total que duplicavam somas e do corte nos dados de 2024 | Recorte (municípios de SP, 2019 a 2023) definido pelo grupo e aprovado pelo mentor |
| Revisão de textos | Revisão crítica dos rascunhos, apontando erros e pontos fracos | Cada seção foi escrita pelo seu responsável e reescrita a partir das revisões |

**Princípios que seguimos:**

- Nenhum número entra no projeto sem que a fonte original seja conferida.
- Cada integrante escreve a própria seção; a IA revisa, não escreve no lugar.
- Todo uso de IA por qualquer integrante é registrado nesta tabela.

---

## Estrutura do repositório

```text
Datasuspeitos/
├── README.md          → apresentação do projeto (esta página)
├── docs/
│   ├── identidade/    → logo, paleta e tipografia
│   └── arquitetura.png
├── data/
│   └── dicionario.md  → o que significa cada coluna usada
├── notebooks/         → análise exploratória (CP2)
└── src/               → tratamento dos dados (CP2)
```

---

## Andamento do projeto

**Checkpoint 1 - Ideação** (entrega de 19 a 23/10/2026)

- [x] Repositório público criado
- [x] Tema e recorte definidos
- [x] Título do projeto
- [ ] Descrição do problema, público e contexto
- [ ] Bases de dados públicas identificadas
- [ ] Tecnologias com justificativa
- [ ] Logo, paleta de cores e tipografia
- [ ] Pitch inicial
- [ ] Todos os integrantes identificados

**Próximas etapas:** Checkpoint 2 — Protótipo (09 a 13/11) · Banca final (07 e 08/12)
