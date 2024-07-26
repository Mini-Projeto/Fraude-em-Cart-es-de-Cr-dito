import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Carregar o conjunto de dados
dataset = pd.read_csv('creditcard.csv')

# Exibir informações gerais sobre o conjunto de dados
dataset.info()

# Verificar a existência de valores nulos
print(dataset.isna().sum())

# Contar o número de linhas duplicadas
duplicadas = dataset.duplicated().sum()
print(f"Número de linhas duplicadas: {duplicadas}")

# Exibir a correlação das variáveis com a variável target 'Class'
print(dataset.corr()['Class'].sort_values(ascending=False))

# Definir variáveis independentes (X) e dependentes (y)
X = dataset.drop('Class', axis=1)
y = dataset['Class']

# Visualização: Dispersão do Tempo vs Montante com distinção de classe
plt.figure(figsize=(10,6))
sns.FacetGrid(dataset, hue='Class', height=6, palette=['blue', 'red']).map(plt.scatter, "Time", "Amount").add_legend()
plt.show()

# Visualização: Mapa de calor da correlação entre variáveis
plt.figure(figsize=(10,6))
sns.heatmap(data=dataset.corr(), cmap='mako')
plt.show()

# Divisão do conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Função para treinar e testar o modelo
def model_train_test(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)  # Treinar o modelo
    prediction = model.predict(X_test)  # Prever com os dados de teste
    
    # Exibir métricas de desempenho
    print(f"Acurácia = {accuracy_score(y_test, prediction)}")
    print(classification_report(y_test, prediction))
    
    # Exibir matriz de confusão
    matrix = confusion_matrix(y_test, prediction)
    grafico = ConfusionMatrixDisplay(matrix)
    grafico.plot()
    plt.show()

# Instanciar modelos
rf_model = RandomForestClassifier()
lr_model = LogisticRegression()

# Treinar e testar os modelos
model_train_test(lr_model, X_train, X_test, y_train, y_test)
model_train_test(rf_model, X_train, X_test, y_train, y_test)
