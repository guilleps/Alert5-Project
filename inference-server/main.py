import tensorflow as tf

model = tf.keras.models.load_model('modelo_nn_optimo.keras')
model.export("models/1") # necesario indicar el numero de la version