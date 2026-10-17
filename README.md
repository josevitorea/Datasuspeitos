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

No estado de São Paulo, entre 2019 e 2023, o acompanhamento gestacional inadequado está associado à incidência de infecções congênitas, evidenciando que cada caso de sífilis congênita representa um atendimento de pré-natal que não se completou de forma efetiva. 
O público afetado engloba gestantes e recém-nascidos em todo o território paulista, com cenários particularmente críticos em municípios da Região Metropolitana, como Osasco e Carapicuíba, onde tanto a taxa de sífilis congênita quanto o percentual de gestantes com menos de 7 consultas estão muito acima da média estadual. 
Em 2023, o estado registrou 4.276 bebês nascidos com sífilis congênita (Painel de Indicadores de Sífilis, Ministério da Saúde), o que representa uma taxa de 8,5 casos a cada 1.000 nascidos vivos, muito acima da meta de eliminação da OPAS/OMS, fixada em 0,5 por 1.000 nascidos vivos. No mesmo período, 82,7% das mães desses bebês realizaram consultas de pré-natal e 66,3% tiveram o diagnóstico da doença identificado durante o acompanhamento. Além disso, dados do SINASC indicam que 17,1% dos bebês nascidos no estado (86.190 crianças em um total de 503.910 nascidos vivos) vieram de mães que realizaram menos de 7 consultas de pré-natal. 
Essa realidade importa porque o agravo é evitável: o diagnóstico é simples e acessível na rotina de acompanhamento, e o tratamento possui baixo custo e alta eficácia no âmbito do SUS. A falha observada não recai sobre as gestantes, mas sim sobre o sistema de cuidado, que não assegura a integralidade do tratamento e o vínculo contínuo. Dessa forma, o projeto conecta-se diretamente às metas 3.1, 3.2 e 3.3 do ODS 3 da Agenda 2030. 

## Público e contexto

O problema afeta diretamente gestantes e recém-nascidos, sobretudo em municípios onde a cobertura e a retenção no pré-natal apresentam maiores fragilidades. A solução desenvolvida destina-se a gestores municipais de saúde e equipes da atenção básica (unidades básicas de saúde), que poderão utilizá-la como ferramenta estratégica para identificar quais municípios prioritários demandam ações imediatas de busca ativa de gestantes, ampliação da testagem e garantia do tratamento completo. 

## Bases de dados

<!-- VITÓRIA: preencha a tabela e escreva as limitações.
     Apague este comentário quando escrever. -->

## Bases de dados

| Base | Fonte | O que usamos | Nível | Período |
|---|---|---|---|---|
| SINASC — Nascidos Vivos | [TabNet / DATASUS](https://datasus.saude.gov.br/informacoes-de-saude-tabnet/) | Nascidos vivos e número de consultas de pré-natal da mãe | Município de residência da mãe | 2019–2023 |
| Painel de Indicadores de Sífilis | [Ministério da Saúde](https://indicadoressifilis.aids.gov.br/) | Casos de sífilis congênita, pré-natal, momento do diagnóstico e tratamento da mãe | Município de residência | 2019–2023 |

As duas bases são unidas pelo **código IBGE do município (6 dígitos)**, formando uma tabela com uma linha por município e ano.

**Limitações conhecidas:**

- **Municípios pequenos têm taxas instáveis.** Em uma cidade com 200 nascimentos, um único caso de sífilis congênita já gera uma taxa de 5 por mil, o que pode colocá-la no topo do ranking por acaso. Por isso, o ranking considera apenas municípios com pelo menos 1.000 nascidos vivos no ano.
- **Subnotificação.** Um município que testa e notifica pouco aparece com menos casos do que tem na realidade, então uma taxa baixa pode ser falsa. Como pouco pré-natal costuma significar pouca testagem, o painel destaca municípios com pré-natal ruim e sífilis baixa como casos a investigar.
- **Período de 2019 a 2023.** Os dados de 2024 ainda não estão consolidados: o Painel de Sífilis vai só até 30/06/2024 e os nascidos vivos, só até 2023. Incluir 2024 mostraria uma queda falsa de casos, causada apenas por registros que ainda não entraram no sistema.
- **Os dados mostram municípios, não pessoas.** As informações de pré-natal e de sífilis estão agregadas por município, em bases separadas, então não é possível ligar cada bebê com sífilis às consultas que a mãe fez. O painel mostra que pré-natal insuficiente e sífilis alta aparecem juntos em um município, mas não prova que as mães com menos consultas são as mesmas dos bebês com sífilis. Por isso, ele serve para priorizar municípios onde agir, e não para explicar a causa de cada caso.
- **Informação ignorada.** No SINASC, parte das declarações não informa o número de consultas (868 em 2023, no estado). Esses registros são excluídos do cálculo do percentual de pré-natal insuficiente.

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

Em 2023, 8,5 a cada 1.000 bebês nasceram com sífilis congênita no estado de São Paulo. E 82,7% das mães desses bebês fizeram pré-natal: estavam no serviço, mas o cuidado não se completou. Para enfrentar esse desafio, o grupo DataSUSpeitos está desenvolvendo um painel analítico interativo que cruza dados de pré-natal e de sífilis congênita por município. O nosso diferencial é integrar essas bases públicas em uma única interface intuitiva, apontando em quais municípios os gestores públicos devem agir primeiro. 

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
- [x] Descrição do problema, público e contexto
- [x] Bases de dados públicas identificadas
- [ ] Tecnologias com justificativa
- [ ] Logo, paleta de cores e tipografia
- [x] Pitch inicial
- [x] Todos os integrantes identificados

**Próximas etapas:** Checkpoint 2 — Protótipo (09 a 13/11) · Banca final (07 e 08/12)
