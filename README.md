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
| Raquel | Problema, contexto, pitch e contato com o mentor | [@usuario](https://github.com/usuario) |
| Vitória | Bases de dados e identidade visual | [@usuario](https://github.com/usuario) |
| José Vitor | Tecnologias, requisitos e protótipo | [@josevitorea](https://github.com/josevitorea) |

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

<!-- KAIKE: o painel, para quem, que decisão apoia (150 a 250 palavras)
     + diagrama da arquitetura em docs/arquitetura.png. Apague este comentário quando escrever. -->

*Em construção.*

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

<!-- KAIKE: em que etapas a IA ajudou e o que foi decidido pelo grupo.
     Apague este comentário quando escrever. -->

*Em construção.*

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
