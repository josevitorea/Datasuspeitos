# Requisitos da solução

**Usuário principal:** gestor municipal ou estadual de saúde e equipes da atenção básica, que precisam decidir **onde priorizar** busca ativa de gestantes, testagem e tratamento da sífilis.

**Legenda:** ✅ essencial para o CP2 (aparece funcionando no protótipo) · ⏳ previsto para depois do CP2

## Requisitos funcionais (o que o painel faz)

| Código | Requisito | CP2 |
|---|---|---|
| RF01 | O gestor vê, para o estado de São Paulo, os 4 números principais do ano escolhido: nascidos vivos, % de mães com menos de 7 consultas de pré-natal, taxa de sífilis congênita por mil nascidos vivos e % de casos com a sífilis da mãe diagnosticada durante o pré-natal. | ✅ |
| RF02 | O gestor acompanha a evolução desses indicadores no estado de 2019 a 2023. | ✅ |
| RF03 | O gestor vê, num quadrante, quais municípios têm **ao mesmo tempo** pré-natal pior e sífilis congênita maior que a média do estado. Esses municípios aparecem destacados como prioritários. | ✅ |
| RF04 | O gestor vê o ranking dos municípios, do mais crítico para o menos crítico, com os três indicadores lado a lado. | ✅ |
| RF05 | O gestor escolhe um município e vê os três indicadores dele de 2019 a 2023, comparados com a média do estado. | ✅ |
| RF06 | O gestor filtra todas as páginas por ano. | ✅ |
| RF07 | O gestor clica num município do ranking e abre direto a página de detalhe dele. | ⏳ |
| RF08 | O gestor vê a taxa de detecção de sífilis em gestantes por município (quantas gestantes com sífilis foram encontradas). | ⏳ |
| RF09 | O gestor vê os municípios agrupados por perfil semelhante (agrupamento com machine learning, sugestão do mentor). | ⏳ |

## Requisitos não funcionais (as regras que a solução respeita)

| Código | Requisito |
|---|---|
| RNF01 | Usa apenas **dados públicos e agregados por município** (SINASC/DATASUS e Painel de Indicadores de Sífilis do Ministério da Saúde). Nenhum dado identifica uma pessoa. |
| RNF02 | É **reprodutível**: qualquer pessoa consegue gerar a tabela e abrir o painel seguindo o README, sem ajuda do grupo. |
| RNF03 | É **atualizável**: quando sair um ano novo, basta baixar os arquivos daquele ano, acrescentá-lo à lista de anos do script e rodar o tratamento de novo. |
| RNF04 | **Confere a qualidade dos dados sozinho**: o script de tratamento para e avisa se encontrar linha repetida, município faltando, contagem impossível ou número do estado diferente do gabarito conferido pelo grupo. |
| RNF05 | O ranking e o quadrante só incluem municípios com **1.000 ou mais nascidos vivos no ano**, para que cidades pequenas não apareçam como críticas por acaso. |
| RNF06 | As cores seguem a identidade visual do projeto, com paleta testada para daltonismo. O laranja é reservado aos municípios prioritários. |
| RNF07 | Roda com ferramentas gratuitas: Python 3, PostgreSQL e Power BI Desktop (Windows). |
