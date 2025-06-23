from tensorflow.keras.models import load_model

MODEL_PATH = "model/modelo_nn_optimo.keras"

try:
    modelo_nn = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error al cargar el modelo: {e}")