# 1° Exemplo com scikit-learn muito usada em inteligência artificial. 
#Regressão Linear.
# pip install -U scikit-learn

from sklearn.linear_model import LinearRegression

# Exemplo de dados de entrada e saída
X = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

# Cria o modelo e ajusta com os dados de entrada e saída
model = LinearRegression()
model.fit(X, y)

# Previsão de um novo valor de entrada
X_test = [[20, 2]]
y_pred = model.predict(X_test)

print(y_pred)