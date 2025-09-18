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
Este é um estudo observacional, transversal e correlacional que investiga como fatores de processo, popularidade, maturidade, atividade e tamanho, se relacionam com métricas internas de qualidade (CBO, DIT, LCOM) em repositórios Java do GitHub. As questões de pesquisa, o conjunto de métricas e a condução geral seguem o escopo definido pelo laboratório, garantindo alinhamento e comparabilidade. Em resumo, queremos entender até que ponto repositórios mais populares, mais antigos, mais ativos ou maiores apresentam padrões diferentes de acoplamento, profundidade de herança e coesão.

---

### 4.1 Coleta de dados
- Para realizar a coleta de dados, foi feito um script em Python, utilizando a Github API, para coletar dados dos 1000 repositórios  open-source mais populares em Java.  
- Para cada repositório foi considerado os seguintes critérios: 
  - **Popularidade**: Números de estrelas do repositório  
  - **Maturidade**: Idade do repositório 
  - **Atividade** : Quantidade de releases
  - **Tamanho do repositório** : LOC e linhas de comentários de cada repositório
  - **CBO** : Coupling Between Objects
  - **DIT** : Depth Inheritance Tree
  - **LCOM** : Lack of Cohesion of Methods
 
As três últimas métricas são relacionadas a métricas de qualidade, onde foram calculadas utilizando a ferramenta CK, uma ferramenta que realiza a análise de código Java.

O script em Python coletou todas as métricas por repositório e consolidou os resultados em um único arquivo CSV, viabilizando a análise direta dos dados brutos.
Além de padronizar a extração (processo e qualidade), o pipeline automatizou o cálculo e o registro das variáveis, reduzindo erros manuais e facilitando a exploração estatística (correlações, comparações por quartis e geração de gráficos).

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
| Número de Stars | 9326,924 |5461,5 | 3667 | 11737.55 | 3155 | 151739 |
| Número de Releases | 40 | 10 | 0 | 116 | 0 | 2215 |
| Idade | 9,45 | 9,65 | 9,07 | 3,08 | 0,17 | 16,67 |
| Tamanho do Repositório (LOC) | 87010 | 14119 | 0 | 6297 | 0 | 170079 |
| CBO | 5 | 5 | 0 | 2 | 0 | 22 |
| DIT | 1,4 | 1,37 | 1 | 0,4 | 0 | 4,39 |
| LCOM | 114 | 23 | 0 | 1740 | 0 | 54800 |
| Número de Linhas Comentadas | 51168 | 5062 | 0 | 422991 | 0 | 12462144 |


---

### 5.2 Análise

#### RQ1 - Popularidade vs Qualidade


A análise mostra que os repositórios mais populares no GitHub, embora recebam mais estrelas, apresentam em média maiores valores de acoplamento (CBO), herança (DIT) e falta de coesão (LCOM) quando comparados aos menos populares. Isso significa que, por dentro, o código dos projetos populares tende a ser mais interligado, mais profundo em hierarquias e menos coeso, refletindo uma estrutura interna mais complexa e difícil de manter. Já os projetos menos populares, apesar de terem menos visibilidade, apresentam em geral uma organização mais simples e coesa, sugerindo que a popularidade não está diretamente associada a uma melhor qualidade interna do código, mas sim a outros fatores como utilidade, comunidade ou marketing.

### Comparação por Quartis de Popularidade (Stars)

| Métrica               | Média (25% mais populares) | Média (25% menos populares) | Variação |
|-----------------------|---------|---------|----------|
| CBO                   | 0,182   | 0,091   | 100%    |
| DIT   | 0,445   | 0,182  | 150%    |
| LCOM           | 3,4   | 8  | -58%    |

#### RQ2 - Maturidade vs Qualidade
 Conforme o repositório amadurece, observa-se uma melhora inicial na qualidade, resultado de refatorações e padronização, mas esse avanço tende a estagnar com o tempo. Ao controlar fatores como tamanho do código, popularidade e cadência de releases, o efeito direto da idade sobre as métricas de qualidade se mostra mínimo ou inexistente. A única exceção parcial foi o LCOM, que apresentou uma leve tendência de melhora em repositórios mais antigos, sugerindo maior coesão interna. No entanto, de forma geral, os dados confirmam que a idade, por si só, não garante qualidade; o que realmente importa é a manutenção contínua, a governança de versões e a gestão da complexidade ao longo do ciclo de vida do projeto.

#### RQ3 - Atividade vs Qualidade

Releases × CBO
 A correlação foi fraca positiva (r ≈ 0,13, p < 0,001). Ou seja, em média, repositórios com mais releases tendem a ter um CBO um pouco maior. O gráfico mostra a maioria dos projetos concentrados perto de zero releases e CBO baixo, mas há alguns casos mais ativos colocando o acoplamento para cima.

Releases × DIT
A correlação foi praticamente nula (r ≈ 0,03, p = 0,38). Ou seja, o número de releases não parece ter relação com a profundidade de herança.

Releases × LCOM
A correlação foi nula (r ≈ -0,01, p = 0,76). A quantidade de releases não influencia na coesão das classes.

A análise mostra que o número de releases não tem relação significativa com a qualidade interna dos repositórios. Apenas no CBO foi encontrada uma correlação fraca positiva, indicando um leve aumento do acoplamento em projetos mais ativos. Já para DIT e LCOM, as correlações foram praticamente nulas, evidenciando que a frequência de releases não influencia de forma relevante nem a profundidade de herança nem a coesão das classes. Isso sugere que a atividade medida por releases não é um bom preditor da qualidade estrutural do código.

#### RQ4 Tamanho vs Qualidade
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

RQ1 - Popularidade vs Qualidade
- **Confirmações e Refutações**:
  - Popularidade ≠ qualidade: não se sustenta após controlar tamanho, LOC e idade. Stars significam escala e não melhor CBO/DIT/LCOM.
  - Cadência de releases: associada a leve melhora, com menos COM/DIT, mas mesmo assim possui um efeito pequeno.
- **❌ Explicações para resultados divergentes**: 
  Popularidade pode ser associadan a projetos maiores, aumenta CBO/LCOM, porem popularidade não melhora o código, há diferenças de domínio /arquitetura, e releases frequentes mostrando cuidado melhor do que estrelas.
- **🔍 Padrões e insights interessantes**: 
  Quanto maior o código, mais cresce a dependência entre partes 
  Comparando projetos de mesmo porte popularidade afeta a qualidade

RQ2 - Maturidade vs Qualidade
- **✅ Confirmações e ❌ Refutações**:
  A hipótese foi apenas parcialmente confirmada. Repositórios mais antigos mostram uma leve melhora na organização interna do código (LCOM), mas em outros pontos como acoplamento (CBO) e herança (DIT) não há sinais claros de ganho com o tempo. Já quando se olha para a maturidade de processo, medida pela frequência de releases, o efeito aparece de forma mais evidente, mostrando que a disciplina de atualização faz mais diferença do que a idade em si.
- **❌ Explicações para resultados divergentes**: 
  Ficar mais velho não garante que o código foi refatorado, muitos crescem em tamanho e acabam ficando mais complexos, escondendo efeitos da idade. Possui casos fora da curva que dsitorcem os números.
- **🔍 Padrões e insights interessantes**: 
  Projetos maiores costumam gerar mais dependências internas e perder coesão. No início da vida do repositório pode haver alguma melhora, mas depois essa evolução tende a parar. Comparando projetos de tamanho parecido, popularidade e idade por si só quase não fazem diferença na qualidade.

RQ03 - Releases vs Qualidade
- **✅ Confirmação ou refutação das hipóteses**: A hipótese IH03 foi refutada, ja que mais releases não indicaram melhor qualidade. Encontrou apenas uma correlação fraca positiva com CBO, sugerindo acoplamento um pouco maior, enquanto para DIT e LCOM não houve relação significativa. 
- **❌ Explicações para resultados divergentes**: A hipótese pode não ter se confirmado porque o número de releases não reflete, necessariamente, a qualidade interna do código, mas sim práticas de versionamento e gestão do projeto. Em alguns casos, projetos grandes podem lançar releases frequentes por exigências de manutenção ou entregas incrementais, sem que isso implique em redução da complexidade interna.   
- **🔍 Padrões e insights interessantes**: Ser antigo não é suficiente, a qualidade só melhora quando há processo, seja releases regulares, revisão, testes. Tamanho pesa muito e pode virar uma bola de neve, inibindo ganhos da maturidade. Em geral há uma arrumada inicial e depois platô, sem manutenção contínua, a qualidade para.

RQ04 - Atividade vs Qualidade
- **✅ Confirmação ou refutação das hipóteses**: A hipótese IH04, que previa que repositórios maiores apresentariam CBO e LCOM mais altos devido à maior complexidade, foi confirmada parcialmente. As correlações de Pearson foram fracas, mas as de Spearman mostraram tendências moderadas e positivas, confirmando que o aumento no tamanho está associado a piora nas métricas de acoplamento e coesão. 
- **❌ Explicações para resultados divergentes**: Os coeficientes de Pearson baixos indicam que a relação não é linear. Isso pode ser explicado pela presença de outliers e pela distribuição desigual de tamanhos: a maior parte dos repositórios é pequena, enquanto poucos projetos muito grandes concentram a tendência de crescimento da complexidade.  
- **🔍 Padrões e insights interessantes**: O LOC é o melhor preditor do aumento das métricas de complexidade, enquanto as linhas de comentários acompanham a mesma direção, mas com efeito menor. Isso reforça que a expansão do código-fonte impacta diretamente na qualidade, enquanto a documentação apenas acompanha esse crescimento.  
  
---

## 6. Conclusão

O estudo mostrou que fatores de processo como popularidade, maturidade, atividade e tamanho se relacionam de maneiras distintas com a qualidade interna do código. A popularidade, medida por estrelas, não se traduziu em melhor organização interna, já que os projetos mais populares tendem a ser maiores e, por isso, mais complexos. A maturidade em termos de idade também não garantiu qualidade: houve sinais de melhora inicial, mas o efeito se mostrou fraco ou inexistente quando controlados outros fatores, reforçando que apenas envelhecer não é suficiente. A atividade medida por releases não se mostrou um bom preditor de qualidade estrutural, aparecendo apenas uma correlação fraca com CBO. Já o tamanho do código foi o fator mais consistente: projetos maiores apresentaram mais acoplamento, heranças mais profundas e menor coesão, confirmando o impacto direto da expansão sobre a complexidade.

No geral, os resultados reforçam que a qualidade de software não depende apenas de popularidade ou idade, mas sim de manutenção contínua, gestão da complexidade e governança de versões. Projetos que crescem sem processos claros tendem a acumular dependências e perder coesão, enquanto aqueles que investem em organização e disciplina de releases têm mais chance de sustentar padrões de qualidade.

---


