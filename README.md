# Desafio_02_Brain

# Objetivo:
O desafio 2 proposto pelo BRAIN consiste no desenvolvimento  e treinamento de um modelo de IA com base no famoso DataFrame do titanic, sendo o objetivo deste, realizar a previsão de sobrevivência de um tripulante baseado nas features escolhidas. O desafio foi resolvido de 2 maneiras diferentes, primeiramente será explicado brevemente a 1ª abordagem utilizada e posteriormente a 2ª abordagem, a qual foi a escolhida no final, a qual foi dividida em 3 etapas:

# 1ª Abordagem:
Está foi uma abordagem padrão adotada para este desafio. Nesta foi realizado:
- O tratamento de dados do DataFrame em questão;
- Transformação de dados categóricos;
- Tratamento de valores nulos;
- Tratamento de outliers;
- Tratamento do DataFrame de teste com os mesmos parâmetros do DataFrame de treino;
- Escolha das features a serem utilizadas;
- Treinamento e validação da IA.

### Outliers dos dados completos:
![alt text](desafio02\imagens\outliers.png)

### Boxplot dos outliers tratados:
![alt text](desafio02\imagens\outliers_tratados.png)

### Resultados obtidos:
- Desempenho aproximado sem tratamento de outliers: 88%
- Desempenho com tratamento de outliers: 99.52%


## Análise de dados:
Cosiste na seleção das features que serão usadas para o treinamento do modelo, esta é feita com base na análise de gráfica e dos dados obtidos atráves da etapa anterior em conjunto com o julgamento do desenvolvedor. Diversos gráficos foram feitos nesta etapa, porém foi mantido apenas aqueles que foram julgados utéis para seleção das features.

### Gráfico de histograma de todas as features selecionadas:
![alt text](desafio02\imagens\histograma_geral.png)

### Matriz de correlação:
![alt text](desafio02\imagens\matriz_correlacao.png)



## Seleção das features:
### Features Mantidas:
  - Pclass: Lógicamente a classe da passagem é muito relevante, devido aos privilégios concedidos para pessoas de classes mais altas, lógica esta que pode ser comprovada através de análise gráfica, onde apesar da maior parte dos tripulantes serem de 3ª classe, podemos observar que a maioria dos sobreviventes foram de 1ª;

    #### Quantidade de sobreviventes por classe:
    ![alt text](desafio02\imagens\sobreviventes_por_classe.png)
  
  - Age: A idade é um fator decisivo na hora de priorizar o salvamento de vidas, esta lógica pode ser reforçada através da análise dos gráficos gerados;

    #### Quantidade de sobreviventes de acordo com a faixa de idade:
    ![alt text](desafio02\imagens\sobreviventes_por_idade.png)

  - SipSp: Feature selecionada através de análise gráfica;

  - Parch: Feature selecionada através de análise gráfica;

  - Fare: Preço da passagem normamente está associado a classe da mesma, esta qual influencia diretamente a chance de sobrevivência de uma pessoa;

  - Sex:  Mulheres normalmente tem prioridade na hora de salvamentos, fato este que poder ser reforçado atráves dos gráficos gerados no notebook, onde apresenta uma alta taxa de sobrevivência das mesmas;

    #### Quantidade de tripulantes:
    ![alt text](desafio02\imagens\pessoas_por_sexo.png)

    #### Sobreviventes por sexo:
    ![alt text](desafio02\imagens\sobreviventes_por_sexo.png)

  - Embarked: Feature selecionada através de análise gráfica;

### Features retiradas:
  - PassengerId: Desnecessário para a IA, sendo somente a contagem da quantidade de passageiros;

  - Survided: Target da IA;

  - Name: Desnecessário para a IA, não é possivel treinar a IA com strings, onde convertendo os nomes seria algo sem sentido;

  - Ticket: Desnecessário para a IA, sendo somente uma forma de identificação da passagem, não tendo influência na taxa de sobrevivência do tripulante;

  - Cabin: Devido a quantidade excessiva de valores nulos, a features foi descartada;



# 2ª Abordagem:
Com as features já decididas foi necessário apenas algumas etapas adicionais.

## Etapa I - Tratamento do DataFrame de testes
Foi realizado uma preparação dos dados do DataFrame para que o modelo de IA possa fazer o teste do modelo que sera criado. Sendo necessário deixar as mesmas features que serão utilizadas no teste do modelo e o tratamento categórico para as remanecentes 

## Etapa II - Desenvolvimento de um modelo para preenchimento de dados:
Realizamos um breve tratamento de dados que consiste no one hot da features categóricas e remoção das que não serão utilizadas. Após isto separamos o DataFrame de treino em dois, o 1º somentos com os dados completos e o 2º com as linhas que possuem valores faltantes, logos após fazemos realizamos o treinamento de um modelo que ira prever os valores nulos presentes na coluna Age (Lógica que poderia ser aplicada a qualquer outra coluna com valores nulos presentes), com o DataFrame de dados_completos, utilizando uma parte para treino e outra para teste utilizando o e modelo Random Forest Regressor obtemos uma taxa de acertividade de 74.35%.

## Etapa II - Desenvolvimento do modelo final:
Com todos os dados preenchidos é realizado o treinamento do modelo final utilizando Regressão Logística, modelo estes que apesar de ter atingido o mesmo desempenho final que o desenvolvido na primeira abordagem (99,52%), possui um resultado melhor quando em teste sem a remoção dos outliers dos dados (este qual remove 3/4 dos dados totais), sendo aproximadamente 92%. 

### Matriz de confusão para validação da IA:
![alt text](desafio02\imagens\matriz_confusao.png)
