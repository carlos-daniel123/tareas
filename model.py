from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r", encoding="utf-8").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index] * 100

    if class_name[2:].startswith("imagenes IA"):
      return f"Tu imagen esta hecha con IA y tiene una precisión del {confidence_score:.2f}% \nlas IAs no comen... a menos de que cuentes los recursos entonces comen mas que la tierra, 32GB de RAM no le bastan, y eso que la hice en Google Teachable Machine, imagina lo que haría con un superordenador"
    
    else:
        return f"Tu imagen es un gato y tiene una precisión del {confidence_score:.2f}% \nLos gatos son carnívoros y se alimentan principalmente de carne, como pollo, pescado, carne de res y alimentos comerciales para gatos que contienen proteínas animales."