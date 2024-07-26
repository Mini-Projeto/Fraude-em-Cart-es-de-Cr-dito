Credit Card Fraud Detection

O projeto teve como fonte uma base de dados retirada do site Kaggle.Este dataset contém transações feitas por cartões de crédito em setembro de 2013 por portadores de cartão europeus. Ele abrange transações realizadas em dois dias, com 492 fraudes entre 284.807 transações, resultando em uma proporção altamente desequilibrada, onde fraudes representam apenas 0,172% das transações.

As variáveis de entrada são exclusivamente numéricas e resultam de uma transformação PCA. Devido a questões de confidencialidade, não são fornecidas as características originais. As variáveis V1, V2, ..., V28 são os componentes principais obtidos com PCA. As únicas variáveis que não foram transformadas são Time e Amount. A variável Time representa o tempo em segundos entre cada transação e a primeira transação do dataset, enquanto Amount é o valor da transação e pode ser usado para aprendizado sensível ao custo. A variável de resposta Class indica fraude (1) ou não (0).

Instalação

1.Clone o repositório para o seu ambiente local:
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git

2.Navegue até o diretório do projeto:
Copiar código
cd nome-do-repositorio

3.Instale os pacotes necessários:
Copiar código
pip install -r requirements.txt

Uso

1.Carregue o conjunto de dados:
Copiar código
dataset = pd.read_csv('creditcard.csv')
2.Execute o script principal para treinar e testar os modelos:
Copiar código
python main.py

Estrutura do Projeto

plaintext
Copiar código
├── README.md
├── creditcard.csv
├── main.py
└── requirements.txt
README.md: Instruções gerais e detalhes do projeto.
creditcard.csv: Conjunto de dados de transações de cartão de crédito.
main.py: Script principal contendo o código para treino e teste dos modelos.
requirements.txt: Arquivo de requisitos com as bibliotecas necessárias para rodar o projeto.
Detalhes do Conjunto de Dados

Time: Número de segundos decorridos entre esta transação e a primeira transação no conjunto de dados.
V1-V28: Variáveis resultantes de uma transformação PCA (Principal Component Analysis) aplicada para proteger informações sensíveis.
Amount: Valor da transação.
Class: Classe de fraude (1) ou não fraude (0).
Modelos Utilizados

Random Forest Classifier: Um modelo de ensemble que usa múltiplas árvores de decisão para melhorar a precisão e controlar o overfitting.
Logistic Regression: Um modelo de regressão linear utilizado para problemas de classificação.
Visualizações

O script inclui visualizações para:

Dispersão de transações ao longo do tempo, distinguindo fraudes e não fraudes.
Mapa de calor das correlações entre as variáveis.
Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Para maiores detalhes, por favor, consulte o CONTRIBUTING.md.

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

