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
| IH03 | Repositórios com maior número de releases tendem a apresentar melhor qualidade, com CBO mais baixo e LCOM menor, pois releases frequentes ajdudam a manter o projeto sempre em dia. |
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

#### RQ1

#### RQ2
Conforme o repositório amadurece, é possível ver uma melhora inicial nas métricas de qualidade seja por refatorações e padronização, mas depois o avanço tende a estagnar. Ao controlar fatores como tamanho do código, LOC, popularidade e cadência de releases, o efeito direto da idade torna-se quase imperceptivel. Com isso, foi possível analisar que não é a idade que garante qualidade, e sim manutenção contínua, governança de versões e gestão da complexidade ao longo do tempo.

#### RQ3 - Atividade vs Qualidade

Releases × CBO
A correlação foi fraca positiva (r ≈ 0,13, p < 0,001). Ou seja, em média, repositórios com mais releases tendem a ter um CBO um pouco maior. O gráfico mostra a maioria dos projetos concentrados perto de zero releases e CBO baixo, mas há alguns casos mais ativos colocando o acoplamento para cima.

Releases × DIT
A correlação foi praticamente nula (r ≈ 0,03, p = 0,38). Ou seja, o número de releases não parece ter relação com a profundidade de herança.

Releases × LCOM
A correlação foi nula (r ≈ -0,01, p = 0,76). A quantidade de releases não influencia na coesão das classes.

A análise mostra que o número de releases não tem relação significativa com a qualidade interna dos repositórios. Apenas no CBO foi encontrada uma correlação fraca positiva, indicando um leve aumento do acoplamento em projetos mais ativos. Já para DIT e LCOM, as correlações foram praticamente nulas, evidenciando que a frequência de releases não influencia de forma relevante nem a profundidade de herança nem a coesão das classes. Isso sugere que a atividade medida por releases não é um bom preditor da qualidade estrutural do código.

#### RQ4 
### Correlação (Pearson) - Tamanho × Qualidade

| Métrica               | CBO médio | DIT médio | LCOM médio |
|-----------------------|---------|---------|----------|
| Loc                   | 0.172   | 0.071   | 0.054    |
| Linhas de comentários   | 0.003   | -0.075  | 0.015    |
| Tamanho total           | 0.081   | -0.011  | 0.033    |

### Correlação (Spearman) - Tamanho × Qualidade

| Métrica             | CBO médio | DIT médio | LCOM médio |
|---------------------|---------|---------|----------|
| loc                 | 0.481   | 0.372   | 0.535    |
| Linhas de comentários | 0.344   | 0.209   | 0.375    |
| Tamanho total          | 0.384   | 0.261   | 0.432    |


Não há relação linear forte, mas existe tendência monotônica clara: repositórios maiores tendem a ter maior acoplamento (CBO), herança um pouco mais profunda (DIT) e menor coesão (LCOM ↑). As linhas de comentário acompanham essa tendência, mas com efeito menor que LOC.
Isso sugere outliers e não linearidade, pois à medida que o tamanho cresce (especialmente no alto da distribuição), as métricas de “complexidade” pioram progressivamente.

---

### 5.4. Discussão dos resultados

- RQ1
- **Confirmações e Refutações**:
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

RQ03 - Releases vs Qualidade
- **✅ Confirmação ou refutação das hipóteses**: A hipótese IH03 foi refutada, ja que mais releases não indicaram melhor qualidade. Encontrou apenas uma correlação fraca positiva com CBO, sugerindo acoplamento um pouco maior, enquanto para DIT e LCOM não houve relação significativa. 
- **❌ Explicações para resultados divergentes**: A hipótese pode não ter se confirmado porque o número de releases não reflete, necessariamente, a qualidade interna do código, mas sim práticas de versionamento e gestão do projeto. Em alguns casos, projetos grandes podem lançar releases frequentes por exigências de manutenção ou entregas incrementais, sem que isso implique em redução da complexidade interna.   
- **🔍 Padrões e insights interessantes**: Apesar da ausência de correlação significativa, observou-se que a maioria dos repositórios permanece próxima de zero releases e com métricas de qualidade baixas, enquanto poucos projetos mais ativos apresentaram CBO um pouco mais elevado. Isso sugere que a atividade em termos de releases pode estar associada apenas a casos específicos, sem constituir uma tendência geral.  

RQ04 - Atividade vs Qualidade
- **✅ Confirmação ou refutação das hipóteses**: A hipótese IH04, que previa que repositórios maiores apresentariam CBO e LCOM mais altos devido à maior complexidade, foi confirmada parcialmente. As correlações de Pearson foram fracas, mas as de Spearman mostraram tendências moderadas e positivas, confirmando que o aumento no tamanho está associado a piora nas métricas de acoplamento e coesão. 
- **❌ Explicações para resultados divergentes**: Os coeficientes de Pearson baixos indicam que a relação não é linear. Isso pode ser explicado pela presença de outliers e pela distribuição desigual de tamanhos: a maior parte dos repositórios é pequena, enquanto poucos projetos muito grandes concentram a tendência de crescimento da complexidade.  
- **🔍 Padrões e insights interessantes**: O LOC é o melhor preditor do aumento das métricas de complexidade, enquanto as linhas de comentários acompanham a mesma direção, mas com efeito menor. Isso reforça que a expansão do código-fonte impacta diretamente na qualidade, enquanto a documentação apenas acompanha esse crescimento.  
  
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

---


