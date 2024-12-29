# ========================================================================================================
print("\n          Paper - ISARC2024\n")
# Section 1: Environment Setup
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os

# Cargar el modelo entrenado
model = load_model("C:/Users/CHRISTOPHER/Desktop/AlgTesis/keras_model.h5", compile=False)

# Cargar las etiquetas
class_names = open("C:/Users/CHRISTOPHER/Desktop/AlgTesis/labels.txt", "r").readlines()

# Directorio que contiene las imágenes de prueba
test_images_dir = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/Bridge"

# Listar todos los archivos en el directorio
image_files = [f for f in os.listdir(test_images_dir) if os.path.isfile(os.path.join(test_images_dir, f))]

for image_file in image_files:
    # Construir la ruta completa de la imagen
    image_path = os.path.join(test_images_dir, image_file)
    # Leer la imagen
    image = cv2.imread(image_path)
    # Redimensionar la imagen a las dimensiones requeridas por tu modelo
    resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Convertir la imagen a un array de numpy y darle forma según las necesidades del modelo
    input_image = resized_image.astype(np.float32).reshape(1, 224, 224, 3)
    
    # Normalizar el array de la imagen
    input_image = (input_image / 127.5) - 1

    # Realizar predicciones con el modelo
    prediction = model.predict(input_image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Imprimir la predicción y la puntuación de confianza para cada imagen
    print(f"Para la imagen {image_file}:")
    print("Clase:", class_name[2:])
    print("Puntuación de confianza:", str(np.round(confidence_score * 100))[:-2], "%")

    # Colorear la imagen según la predicción
    if class_name == "GRIETA":
        overlay_color = np.array([0, 0, 255])  # rojo tenue para grietas
        alpha = 0.1  # ajusta la transparencia (entre 0 y 1)
        # Mezclar directamente las imágenes
        image = cv2.addWeighted(resized_image, 1 - alpha, overlay_color, alpha, 0)

    # Mostrar la imagen coloreada
    cv2.imshow('Imagen', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()