import tensorflow as tf

try:
    model = tf.keras.models.load_model(r"C:\Users\Vivtus\Desktop\ML Project\my_bilstm_model.keras")
    print("✅ Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
