
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


caminho_csv = 'creditcard.csv'
dataset = pd.read_csv(caminho_csv)

#Texto p código
texto1 = '''dataset.isna().sum()
dataset.duplicated().sum()'''
texto2 = '''X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.5, random_state=42)'''
texto3 = '''def model_train_test(model, X_train, X_test, y_train, y_test):
  model.fit(X_train,y_train)
  prediction = model.predict(X_test)
  print("acurracy = {}" .format(accuracy_score(y_test,prediction)))
  print(classification_report(y_test,prediction))
  matrix = confusion_matrix(y_test,prediction)
  grafico = ConfusionMatrixDisplay(matrix)
  grafico.plot()
  plt.show()'''

#Gráfico p Analise de dados
plt.figure(figsize = (10,6))
sns.heatmap(data=dataset.corr(), cmap = 'mako' )
plt.show()


st.set_page_config(page_title='Mini Projeto')
st.subheader('Mini-Projeto')
st.title('Fraude em Cartões de Crédito')

    #st.header('Introdução à Base de dados')
with st.container():
    st.header('Introdução à Base de dados')
    st.write('O projeto teve como fonte uma base de dados retirada do site Kaggle.Este dataset contém transações feitas por cartões de crédito em setembro de 2013 por portadores de cartão europeus. Ele abrange transações realizadas em dois dias, com 492 fraudes entre 284.807 transações, resultando em uma proporção altamente desequilibrada, onde fraudes representam apenas 0,172% das transações.')
    st.write('As variáveis de entrada são exclusivamente numéricas e resultam de uma transformação PCA. Devido a questões de confidencialidade, não são fornecidas as características originais. As variáveis **V1, V2, ..., V28** são os componentes principais obtidos com PCA. As únicas variáveis que não foram transformadas são **Time** e **Amount**. A variável **Time** representa o tempo em segundos entre cada transação e a primeira transação do dataset, enquanto **Amount** é o valor da transação e pode ser usado para aprendizado sensível ao custo. A variável de resposta **Class** indica fraude (1) ou não (0).')
    st.image('cartões de crédito.jpg', caption='Fonte: Designed by FreePik')

   #st.header('Tratamento de Dados')
with st.container():
    st.write('---')
    st.header('Tratamento de Dados')
    st.write('Abaixo, você encontrará uma visualização das primeiras linhas da base de dados,permitindo uma visão geral da estrutura dos dados')
    st.write(dataset.head())
    st.write('  Antes da análise dos dados,foi feita uma limpeza na base de modo a retirar as linhas duplicadas ou que tivessem algum número/elemento faltante.Para isso foi utilizados o código a seguir para detectar se havia alguma linha com problemas.')
    st.code(texto1, line_numbers=False)
    st.write('')

    #st.header('Análise dos Dados')
with st.container():
    st.write('---')
    st.header('Análise dos Dados')
    st.write('No gráfico abaixo, apresentamos uma análise das transações de cartão de crédito, onde são identificadas tanto as transações corretas quanto as fraudulentas ao longo do tempo. O eixo horizontal representa o tempo **(Time)** das transações, enquanto o eixo vertical indica o valor das transações **(Amount)**.')
    st.write('Cada ponto no gráfico simboliza uma transação individual, sendo que a cor do ponto diferencia se a transação foi legítima ou fraudulenta:')
    st.write(' - Os pontos em azul **(Class 0)** representam as transações corretas.')
    st.write(' - Os pontos em vermelho **(Class 1)** indicam as transações fraudulentas.')
    st.image('grafico 1.png', caption='Fonte: Autores')
    st.write('Esta visualização permite observar a distribuição das transações ao longo do tempo e analisar padrões entre as transações corretas e fraudulentas. Notamos que, apesar da maioria das transações serem legítimas, há uma presença distinta de fraudes que pode ser investigada mais a fundo para entender os comportamentos e características dessas ocorrências.')
    st.write('No gráfico abaixo, apresentamos uma matriz de correlação que mostra as relações entre diferentes variáveis de um conjunto de dados de transações de cartão de crédito. A correlação é uma medida estatística que indica a força e a direção do relacionamento linear entre duas variáveis. Os valores de correlação variam de -1 a 1')
    st.pyplot(plt)
    st.write('A análise desta matriz pode ajudar a identificar quais variáveis estão mais fortemente relacionadas entre si, o que pode ser útil para a construção de modelos preditivos e para a compreensão dos padrões subjacentes aos dados.')

    #st.header('Algoritmo de Resolução')
with st.container():
    st.write('---')
    st.header('Algoritmo de Resolução')
    st.write('O código a seguir apresenta um algoritmo para treinar e testar modelos de aprendizado de máquina usando os dados. Este algoritmo é projetado para avaliar a performance de um modelo na detecção de fraudes em transações.')
    st.code(texto2, line_numbers=False)
    st.write('O conjunto de dados é dividido em duas partes: treinamento (X_train e y_train) e teste (X_test e y_test). Aqui, X representa as características das transações e y representa os rótulos (0 para transações legítimas e 1 para fraudes). A divisão é feita de forma que 50% dos dados sejam usados para treinamento e 50% para teste.')
    st.write('A função a seguir serve para treinar e testar um modelo de aprendizado de máquina usando um conjunto de dados de transações de cartão de crédito. Ela divide os dados em treinamento e teste, treina o modelo nos dados de treinamento e faz previsões com os dados de teste. Em seguida, calcula e exibe a acurácia do modelo, gera um relatório de classificação com métricas detalhadas (como precisão, recall e F1-score) e exibe uma matriz de confusão que visualiza a distribuição de previsões corretas e incorretas. Essa função é útil para avaliar a eficácia de um modelo na detecção de fraudes em transações.')
    st.code(texto3, line_numbers=False)

with st.container():
    st.write('---')
    st.header('Resultados')
    st.write('A seguir serão expostos obtidos pelo modelo.Ainda, ressalta-se que o modelo utilizado foi o Random Forest Classifier, um algoritmo de aprendizado de máquina de ensemble que utiliza múltiplas árvores de decisão para melhorar a precisão e reduzir o risco de overfitting.')
    st.image('grafico final.png', caption='Fonte: Autores')
    st.write('Os resultados indicam uma alta acurácia de 99,95%, o que significa que o modelo classificou corretamente a maioria das transações. A matriz de confusão revela que, de 142.404 transações no conjunto de teste, 142.148 foram corretamente classificadas como não fraudulentas (classe 0) e 186 como fraudulentas (classe 1). Houve apenas 10 falsos positivos (transações classificadas incorretamente como fraudulentas) e 60 falsos negativos (transações fraudulentas classificadas incorretamente como não fraudulentas).')
    st.write('O relatório de classificação detalha métricas importantes:')
    st.write(' - Precision: A precisão para a classe 0 é de 1.00 (100%), indicando que todas as transações classificadas como não fraudulentas realmente não eram fraudulentas. Para a classe 1, a precisão é de 0.95 (95%).')
    st.write(' - Recall: O recall para a classe 0 é de 1.00 (100%), mostrando que todas as transações não fraudulentas foram corretamente identificadas. Para a classe 1, o recall é de 0.76 (76%), indicando que 76% das fraudes foram corretamente identificadas.')
    st.write(' - F1-Score: A pontuação F1 para a classe 0 é de 1.00 (100%), e para a classe 1 é de 0.84 (84%), um equilíbrio entre precisão e recall.')
    st.write(' - Support: O suporte mostra o número de ocorrências reais de cada classe no conjunto de teste (142.158 para a classe 0 e 246 para a classe 1).')