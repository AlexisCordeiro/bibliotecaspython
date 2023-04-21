# 4° TensorFlow, biblioteca muito usada em redes neurais e aprendizado de máquina.
import tensorflow as tf

# Definindo os dados de treinamento
x_train = [1.0, 2.0, 3.0, 4.0]
y_train = [2.0, 4.0, 6.0, 8.0]

# Definindo o modelo da rede neural
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilando o modelo
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

# Treinando o modelo
model.fit(x_train, y_train, epochs=100)

# Testando o modelo
x_test = [5.0, 6.0, 7.0, 8.0]
y_test = model.predict(x_test)
print(y_test)
