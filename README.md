# 📝 Template de Relatório Técnico de Laboratório

## 1. Informações do grupo
- **🎓 Curso:** Engenharia de Software
- **📘 Disciplina:** Laboratório de Experimentação de Software
- **🗓 Período:** 6° Período
- **👨‍🏫 Professor(a):** Prof. Dr. Wesley Dias Maciel
- **👥 Membros do Grupo:** Sophia Mendes, Thiago Andrade

---

## 2. Introdução
O laboratório tem como objetivo analisar a maturidade e o nível de atividade de sistemas populares hospedados em repositórios públicos.  
Espera-se compreender padrões de desenvolvimento, adoção de linguagens e engajamento da comunidade em projetos open-source.

### 2.1. Questões de Pesquisa (Research Questions – RQs)
As **Questões de Pesquisa** foram definidas para guiar a investigação e estruturar a análise dos dados coletados:

**🔍 Questões de Pesquisa - Research Questions (RQs):**

| RQ   | Pergunta |
|------|----------|
| RQ01 | Qual a relação entre a popularidade dos repositórios e as suas características de
qualidade? |
| RQ02 | Qual a relação entre a maturidade do repositórios e as suas características de
qualidade ? |
| RQ03 | Qual a relação entre a atividade dos repositórios e as suas características de
qualidade? |
| RQ04 | Qual a relação entre o tamanho dos repositórios e as suas características de
qualidade? |

### 2.2. Hipóteses Informais (Informal Hypotheses – IH)
As **Hipóteses Informais** foram elaboradas a partir das RQs, estabelecendo expectativas sobre os resultados esperados do estudo:

**💡 Hipóteses Informais - Informal Hypotheses (IH):**

| IH   | Descrição |
|------|-----------|
| IH01 | Repositórios populares têm melhores médias de qualidade. |
| IH02 | Repositorios com mais qualidade são mais maduros |
| IH04 | Repositórios populares tendem a ser escritos nas linguagens mais utilizadas (ex.: JavaScript, Python, Java), representando a adoção de linguagens consolidadas. |
| IH05 | Mais de 50% dos repositórios populares recebem atualizações nos últimos 3 meses, refletindo atividade contínua da comunidade. |
| IH06 | Projetos populares com maior número de forks tendem a ter mais pull requests aceitas, indicando engajamento externo significativo. |
| IH07 | Repositórios populares com grande número de stars podem apresentar Big Numbers em métricas como número de commits, branches e releases, destacando sua relevância na comunidade open-source. |

---

## 3. Tecnologias e ferramentas utilizadas
- **💻 Linguagem de Programação:** [Python]
- **🛠 Frameworks/Bibliotecas:** [CK]
- **🌐 APIs utilizadas:** [GitHub REST API]
- **📦 Dependências:** [time, subprocess, csv, shutil, pathlib, datetime, requests, re]

---

## 4. Metodologia
Este é um estudo observacional, transversal e correlacional que investiga como fatores de processo — popularidade, maturidade, atividade e tamanho — se relacionam com métricas internas de qualidade (CBO, DIT, LCOM) em repositórios Java do GitHub. Não há intervenção: analisamos dados tal como estão nos projetos. As questões de pesquisa, o conjunto de métricas e a condução geral seguem o escopo definido pelo laboratório, garantindo alinhamento e comparabilidade. Em resumo, queremos entender até que ponto repositórios mais populares, mais antigos, mais ativos ou maiores apresentam padrões diferentes de acoplamento, profundidade de herança e coesão.

---

### 4.1 Coleta de dados
- A coleta foi realizada utilizando a **GitHub API**, que fornece acesso estruturado a metadados de repositórios.  
- Foram considerados [X] repositórios, selecionados a partir dos seguintes critérios:  
  - **Popularidade** → ex.: repositórios com maior número de estrelas (top-N).  
  - **Relevância por linguagem** → restrição a uma linguagem de programação específica.  
  - **Atividade mínima** → presença de commits, issues ou releases nos últimos anos.  
- Cada repositório retornou informações brutas como datas de criação e atualização, número de estrelas, forks, issues, releases e linguagem principal.  

---

### 4.2 Filtragem e paginação
- A API do GitHub retorna resultados de até 100 itens por página, e como a busca deveria ser nos 1000 repositorios de Java mais populosos, a paginação foi necessaria para impedir instabilidades,como timeouts, quedas intermitentes, caso uma pagina falhe o script reexecuta apenas para aquela pagina, sem perda de progressos anteriores. 

---

### 4.3 Ordem das etapas (clone → CK → métricas)
- Após coletar os identificadores pela API do GitHub, fizemos o clone local de cada repositório. Com o repositório do CK integrado ao projeto, executamos a ferramenta para extrair métricas dos 1000 repositorios clonados, incluindo CBO, DIT, LCOM, LOC e total de classes. Em seguida, geramos um arquivo CSV das metricas colhidas, para posteriormente serem analisadas.

---

### 4.4 Principais problemas técnicos encontrados
° Limite de 256 bytes: nos títulos de arquivos, pastas ou caminhos de alguns repositorios, extrapolavam o limite aceito de 256 bytes. Quando isso acontecia, o CK não conseguia ler aqueles artefatos e a análise quebrava. Incluímos tratamento para pular esses casos e registrar o erro para auditoria.

° Suporte limitado do CK a frameworks modernos: o CK não lida bem com estruturas mais novas de alguns frameworks. Isso gerou muitas falhas e interrupções durante a execução do CK na análise.

---

### 4.5 Custo temporal
Somando clones, reexecuções e as rodadas de CK, o processo completo passou de 16 horas até concluir todo o conjunto. Esse tempo reflete tanto o volume, de 1.000 repositorios, quanto as repetições em casos de interrupções e falhas, fora as limitações da ferramenta CK, em relação a leitura de repositórios específicos.

---

### 4.6 Métricas

Inclua métricas relevantes de repositórios do GitHub, separando **métricas do laboratório** e **métricas adicionais trazidas pelo grupo**:

#### 📊 Métricas de Laboratório - Lab Metrics (LM)
| Código | Métrica | Descrição |
|--------|---------|-----------|
| LM01 | 🕰 Idade do Repositório (anos) | Tempo desde a criação do repositório até o momento atual, medido em anos. |
| LM02 | ✅ Pull Requests Aceitas | Quantidade de pull requests que foram aceitas e incorporadas ao repositório. |
| LM03 | 📦 Número de Releases | Total de versões ou releases oficiais publicadas no repositório. |
| LM04 | ⏳ Tempo desde a Última Atualização (dias) | Número de dias desde a última modificação ou commit no repositório. |
| LM05 | 📋 Percentual de Issues Fechadas (%) | Proporção de issues fechadas em relação ao total de issues criadas, em percentual. |
| LM06 | ⭐ Número de Estrelas | Quantidade de estrelas recebidas no GitHub, representando interesse ou popularidade. |
| LM07 | 🍴 Número de Forks | Número de forks, indicando quantas vezes o repositório foi copiado por outros usuários. |
| LM08 | 📏 Tamanho do Repositório (LOC) | Total de linhas de código (Lines of Code) contidas no repositório. |

#### 💡 Métricas adicionais trazidas pelo grupo - Additional Metrics (AM)
| Código | Métrica | Descrição |
|--------|---------|-----------|
| AM01 | 💻 Linguagem Primária | Linguagem de programação principal do repositório (ex.: Python, JavaScript, Java) |
| AM02 | 🔗 Forks vs Pull Requests Aceitas | Relação entre número de forks e pull requests aceitas |
| AM03 | 📈 Evolução Temporal | Evolução temporal de releases e pull requests aceitas |
| AM04 | 🌟 Big Numbers | Métricas com valores expressivos (commits, branches, stars, releases) |

> Obs.: Adapte ou acrescente métricas conforme o seu dataset.

---

### 4.5 Cálculo de métricas
- As métricas definidas na seção **4.4** foram obtidas a partir de dados brutos retornados pela **GitHub API**.  
- Para cada métrica, foram aplicadas operações de transformação simples, tais como:  
  - **Diferença de datas** → cálculo da idade do repositório e tempo desde a última atualização.  
  - **Contagens absolutas** → número de pull requests aceitas, releases, forks e estrelas.  
  - **Proporções** → percentual de issues fechadas em relação ao total.  
  - **Identificação categórica** → linguagem primária de cada repositório.  
- Em alguns casos, os valores foram agregados em séries temporais para observar **evolução ao longo do tempo** (ex.: releases e pull requests).  
- Além das métricas individuais, foi proposto um **índice composto de popularidade**, calculado como uma **combinação linear ponderada** de métricas representativas (⭐ estrelas, 🍴 forks, 📦 releases, ✅ pull requests aceitas). Esse índice foi utilizado para ranqueamento complementar e comparação entre repositórios.  

---

### 4.6 Ordenação e análise inicial
- Repositórios ordenados pelo **índice composto de popularidade** ou, alternativamente, pelo número de estrelas.  
- A análise inicial foi conduzida a partir de **valores medianos, distribuições** e **contagem de categorias** (como linguagens e tipos de contribuições).  
- Essa etapa teve como objetivo fornecer uma **visão exploratória** do dataset, identificando padrões gerais antes de análises mais detalhadas.  

---

### 4.7. Relação das RQs com as Métricas
As **Questões de Pesquisa (Research Questions – RQs)** foram associadas a métricas específicas, previamente definidas na seção de métricas (Seção 4.4), garantindo que a investigação seja **sistemática e mensurável**.  

A tabela a seguir apresenta a relação entre cada questão de pesquisa e as métricas utilizadas para sua avaliação:

**🔍 Relação das RQs com Métricas:**

| RQ   | Pergunta | Métrica utilizada | Código da Métrica |
|------|----------|------------------|------------------|
| RQ01 | Sistemas populares são maduros/antigos? | 🕰 Idade do repositório (calculado a partir da data de criação) | LM01 |
| RQ02 | Sistemas populares recebem muita contribuição externa? | ✅ Total de Pull Requests Aceitas | LM02 |
| RQ03 | Sistemas populares lançam releases com frequência? | 📦 Total de Releases | LM03 |
| RQ04 | Sistemas populares são atualizados com frequência? | ⏳ Tempo desde a última atualização (dias) | LM04 |
| RQ05 | Sistemas populares são escritos nas linguagens mais populares? | 💻 Linguagem primária de cada repositório | AM01 |
| RQ06 | Sistemas populares possuem um alto percentual de issues fechadas? | 📋 Razão entre número de issues fechadas pelo total de issues | LM05 |
| RQ07 | Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência? | ✅ Pull Requests Aceitas, 📦 Número de Releases, ⏳ Tempo desde a Última Atualização, 💻 Linguagem primária | LM02, LM03, LM04, AM01 |

---

## 5. Resultados

 -RQ1

- RQ2
Conforme o repositório amadurece, é possível ver uma melhora inicial nas métricas de qualidade seja por refatorações e padronização, mas depois o avanço tende a estagnar. Ao controlar fatores como tamanho do código, LOC, popularidade e cadência de releases, o efeito direto da idade torna-se quase imperceptivel. Com isso, foi possível analisar que não é a idade que garante qualidade, e sim manutenção contínua, governança de versões e gestão da complexidade ao longo do tempo.

---

### 5.1 Distribuição por categoria

Para métricas categóricas, como linguagem de programação, faça contagens e tabelas de frequência:

| Linguagem | Quantidade de Repositórios |
|---------------|------------------------|
| 🐍 Python     | 350                    |
| 💻 JavaScript | 300                    |
| ☕ Java        | 200                    |
| 📦 Outros     | 150                    |

---

### 5.2 Estatísticas Descritivas

Apresente as estatísticas descritivas das métricas analisadas, permitindo uma compreensão mais detalhada da distribuição dos dados.

| Métrica | Média | Mediana | Moda | Desvio Padrão | Mínimo | Máximo |
|---------|------|--------|-----|---------------|--------|--------|
| Número de Stars | 9327 | 5462 | 3667 | 11738 | 3155 | 151739 |
| Número de Releases | 40 | 10 | 0 | 116 | 0 | 2215 |
| Idade | 9,45 | 9,65 | 9,07 | 3,08 | 0,17 | 16,67 |
| Tamanho do Repositório (LOC) | 87010 | 14119 | 0 | 6297 | 0 | 170079 |
| CBO | 5 | 5 | 0 | 2 | 0 | 22 |
| DIT | 1,4 | 1,37 | 1 | 0,4 | 0 | 4,39 |
| LCOM | 114 | 23 | 0 | 1740 | 0 | 54800 |
| Número de Classes | 1599 | 325 | 0 | 6297 | 0 | 170079 |
| Número de Linhas Comentadas | 51168 | 5062 | 0 | 422991 | 0 | 12462144 |
| Número de Arquivos Java | 1369 | 255 | 1 | 6296 | 0 | 153099 |

> 💡 Dica: Inclua gráficos como histogramas ou boxplots junto com essas estatísticas para facilitar a interpretação.

---

### 5.3 Gráficos

Para criar visualizações das métricas, recomenda-se utilizar como referência o projeto **Seaborn Samples**:  
- 🔗 Repositório: [Projeto Seaborn Samples](https://github.com/joaopauloaramuni/laboratorio-de-experimentacao-de-software/tree/main/PROJETOS/Projeto%20Seaborn%20Samples)

- **📊 Histograma**: `grafico_histograma.png` → distribuição de idade, PRs aceitas ou estrelas.  
- **📈 Boxplot**: `grafico_boxplot.png` → dispersão de métricas como forks, issues fechadas ou LOC.  
- **📊 Gráfico de Barras**: `grafico_barras.png` → comparação de métricas entre linguagens.  
- **🥧 Gráfico de Pizza**: `grafico_pizza.png` → percentual de repositórios por linguagem.  
- **📈 Gráfico de Linha**: `grafico_linha.png` → evolução de releases ou PRs ao longo do tempo.  
- **🔹 Scatterplot / Dispersão**: `grafico_dispersao.png` → relação entre estrelas e forks.  
- **🌡 Heatmap**: `grafico_heatmap.png` → correlação entre métricas (idade, PRs, stars, forks, issues).  
- **🔗 Pairplot**: `grafico_pairplot.png` → análise de múltiplas métricas simultaneamente.  
- **🎻 Violin Plot**: `grafico_violin.png` → distribuição detalhada de métricas por subgrupo.  
- **📊 Barras Empilhadas**: `grafico_barras_empilhadas.png` → comparação de categorias dentro de métricas.

> 💡 Dica: combine tabelas e gráficos para facilitar a interpretação e evidenciar padrões nos dados.

---

### 5.4. Discussão dos resultados

Nesta seção, compare os resultados obtidos com as hipóteses informais levantadas pelo grupo no início do experimento.

- RQ1
- **✅ Confirmações e ❌ Refutações**:
  ❌ Popularidade != qualidade: não se sustenta após controlar tamanho, LOC e idade. Stars significam escala e não melhor CBO/DIT/LCOM.
  ✅ Cadência de releases: associada a leve melhora, com menos COM/DIT, mas mesmo assim possui um efeito pequeno.
  ✅ Platô com a idade: melhora no início e estagna depois.
- **❌ Explicações para resultados divergentes**: 
  Popularidade pode ser associadan a projetos maiores, aumenta CBO/LCOM, porem idade não melhora o código, há diferenças de domínio /arquitetura, e releases frequentes mostrando cuidado melhor do que estrelas.
- **🔍 Padrões e insights interessantes**: 
  Quanto maior o código, mais cresce a dependência entre partes 
  Com o tempo há melhora inicial e depois platô
  Comparando projetos de mesmo porte e idade, popularidade e a própria idade quase não fazem diferença

- RQ2
- **✅ Confirmações e ❌ Refutações**:
  ❌ Popularidade != qualidade: não se sustenta após controlar tamanho, LOC e idade. Stars significam escala e não melhor CBO/DIT/LCOM.
  ✅ Cadência de releases: associada a leve melhora, com menos COM/DIT, mas mesmo assim possui um efeito pequeno.
  ✅ Platô com a idade: melhora no início e estagna depois.
- **❌ Explicações para resultados divergentes**: 
  Popularidade pode ser associadan a projetos maiores, aumenta CBO/LCOM, porem idade não melhora o código, há diferenças de domínio /arquitetura, e releases frequentes mostrando cuidado melhor do que estrelas.
- **🔍 Padrões e insights interessantes**: 
  Quanto maior o código, mais cresce a dependência entre partes 
  Com o tempo há melhora inicial e depois platô
  Comparando projetos de mesmo porte e idade, popularidade e a própria idade quase não fazem diferença


- **✅ Confirmação ou refutação das hipóteses**: identifique quais hipóteses foram confirmadas pelos dados e quais foram refutadas.  
- **❌ Explicações para resultados divergentes**: caso algum resultado seja diferente do esperado, tente levantar possíveis causas ou fatores que possam ter influenciado.  
- **🔍 Padrões e insights interessantes**: destaque tendências ou comportamentos relevantes observados nos dados que não haviam sido previstos nas hipóteses.  
- **📊 Comparação por subgrupos (opcional)**: se houver segmentação dos dados (ex.: por linguagem de programação, tamanho do repositório), discuta como os resultados se comportam em cada grupo.

> Relacione sempre os pontos observados com as hipóteses informais definidas na introdução, fortalecendo a análise crítica do experimento.

---

## 6. Conclusão

Resumo das principais descobertas do laboratório.

- **🏆 Principais insights:**  
  - Big numbers encontrados nos repositórios, popularidade e métricas destacadas.  
  - Descobertas relevantes sobre padrões de contribuição, releases, issues fechadas ou linguagens mais utilizadas.  
  - Confirmações ou refutações das hipóteses informais levantadas pelo grupo.

- **⚠️ Problemas e dificuldades enfrentadas:**  
  - Limitações da API do GitHub e paginação de grandes volumes de dados.  
  - Normalização e tratamento de dados inconsistentes ou ausentes.  
  - Desafios com cálculos de métricas ou integração de múltiplos arquivos CSV.  

- **🚀 Sugestões para trabalhos futuros:**  
  - Analisar métricas adicionais ou aprofundar correlações entre métricas de qualidade e métricas de processo.  
  - Testar outras linguagens de programação ou frameworks.  
  - Implementar dashboards interativos para visualização de grandes volumes de dados.  
  - Explorar métricas de tendências temporais ou evolução de repositórios ao longo do tempo.

---

## 7. Referências
Liste as referências bibliográficas ou links utilizados.
- [📌 GitHub API Documentation](https://docs.github.com/en/graphql)
- [📌 CK Metrics Tool](https://ckjm.github.io/)
- [📌 Biblioteca Pandas](https://pandas.pydata.org/)
- [📌 Power BI](https://docs.microsoft.com/en-us/power-bi/fundamentals/service-get-started)

---

## 8. Apêndices
- 💾 Scripts utilizados para coleta e análise de dados.
- 🔗 Consultas GraphQL ou endpoints REST.
- 📊 Planilhas e arquivos CSV gerados.

---
