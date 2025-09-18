# 📝 Template de Relatório Técnico de Laboratório

## 1. Informações do grupo
- **🎓 Curso:** Engenharia de Software
- **📘 Disciplina:** Laboratório de Experimentação de Software
- **🗓 Período:** 6° Período
- **👨‍🏫 Professor(a):** Prof. Dr. Wesley Dias Maciel
- **👥 Membros do Grupo:** Sophia Mendes, Thiago Andrade

---

## 2. Introdução
Este trabalho analisa a relação entre as características do processo de desenvolvimento e a qualidade interna do código em software de código aberto. Focando nos 1.000 repositórios Java mais populares do GitHub, o estudo correlaciona métricas de processo da plataforma com métricas de qualidade de produto, calculadas pela ferramenta de análise estática CK, para investigar como a colaboração distribuída impacta atributos como modularidade e manutenibilidade.

### 2.1. Questões de Pesquisa (Research Questions – RQs)
As **Questões de Pesquisa** foram definidas para guiar a investigação e estruturar a análise dos dados coletados:

**🔍 Questões de Pesquisa - Research Questions (RQs):**

| RQ   | Pergunta |
|------|----------|
| RQ01 | Qual a relação entre a popularidade dos repositórios e as suas características de qualidade? |
| RQ02 | Qual a relação entre a maturidade do repositórios e as suas características de qualidade ? |
| RQ03 | Qual a relação entre a atividade dos repositórios e as suas características de qualidade? |
| RQ04 | Qual a relação entre o tamanho dos repositórios e as suas características de qualidade? |

### 2.2. Hipóteses Informais (Informal Hypotheses – IH)
As **Hipóteses Informais** foram elaboradas a partir das RQs, estabelecendo expectativas sobre os resultados esperados do estudo:

**💡 Hipóteses Informais - Informal Hypotheses (IH):**

| IH   | Descrição |
|------|-----------|
| IH01 | Repositórios populares têm melhores médias de qualidade. |
| IH02 | Repositorios com mais qualidade são mais maduros |
| IH03 | Repositórios com maior número de releases tendem a apresentar melhor qualidade, com CBO mais baixo e LCOM menor, pois releases frequentes ajdudam a manter o projeto sempre em dia.
| IH04 | Repositórios com maior número de linhas de código e classes tendem a apresentar CBO e LCOM mais altos, pois o crescimento do sistema o torna mais complexo de manter tudo modular e legível |

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

#### 📊 Métricas de Laboratório - Lab Metrics (LM)
| Código | Métrica | Descrição |
|--------|---------|-----------|
| LM01 | Número de estrelas | Tempo desde a criação do repositório até o momento atual, medido em anos. |
| LM02 | Tamanho do repositório  | Total de linhas de código e linhas de comentários contidas no repositório. |
| LM03 | Número de Releases | Total de versões ou releases oficiais publicadas no repositório. |
| LM04 | Maturidade do repositório | Número de dias desde a última modificação ou commit no repositório. |
| LM05 | CBO - Coupling between objects | Indicador que mensura o grau de acoplamento entre classes, refletindo a dependência de uma classe em relação a outras. |
| LM06 | DIT - Depth Inheritance Tree | Métrica que expressa a profundidade da árvore de herança, representando o nível hierárquico de uma classe.  |
| LM07 | LCOM - Lack of Cohesion of Methods | Medida que avalia a coesão interna de uma classe, verificando a relação funcional entre seus métodos.  |

---


## 5. Resultados

 -RQ1

- RQ2
Conforme o repositório amadurece, é possível ver uma melhora inicial nas métricas de qualidade seja por refatorações e padronização, mas depois o avanço tende a estagnar. Ao controlar fatores como tamanho do código, LOC, popularidade e cadência de releases, o efeito direto da idade torna-se quase imperceptivel. Com isso, foi possível analisar que não é a idade que garante qualidade, e sim manutenção contínua, governança de versões e gestão da complexidade ao longo do tempo.


### 5.1 Estatísticas Descritivas

Apresente as estatísticas descritivas das métricas analisadas, permitindo uma compreensão mais detalhada da distribuição dos dados.

| Métrica | Média | Mediana | Moda | Desvio Padrão | Mínimo | Máximo |
|---------|------|--------|-----|---------------|--------|--------|
| Número de Stars | 9326,924 |5461.5 | 3667 | 11737.55 | 3155 | 151739 |
| Número de Releases | 40 | 10 | 0 | 116 | 0 | 2215 |
| Idade | 9,45 | 9,65 | 9,07 | 3,08 | 0,17 | 16,67 |
| Tamanho do Repositório (LOC) | 87010 | 14119 | 0 | 6297 | 0 | 170079 |
| CBO | 5 | 5 | 0 | 2 | 0 | 22 |
| DIT | 1,4 | 1,37 | 1 | 0,4 | 0 | 4,39 |
| LCOM | 114 | 23 | 0 | 1740 | 0 | 54800 |
| Número de Linhas Comentadas | 51168 | 5062 | 0 | 422991 | 0 | 12462144 |


---

### 5.2 Análise

#### RQ3 - Atividade vs Qualidade

Releases × CBO
A correlação foi fraca positiva (r ≈ 0,13, p < 0,001). Ou seja, em média, repositórios com mais releases tendem a ter um CBO um pouco maior. O gráfico mostra a maioria dos projetos concentrados perto de zero releases e CBO baixo, mas há alguns casos mais ativos colocando o acoplamento para cima.

Releases × DIT
A correlação foi praticamente nula (r ≈ 0,03, p = 0,38). Ou seja, o número de releases não parece ter relação com a profundidade de herança.

Releases × LCOM
A correlação foi nula (r ≈ -0,01, p = 0,76). A quantidade de releases não influencia na coesão das classes.

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
