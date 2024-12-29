import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import shutil
import os
import matplotlib.pyplot as plt

img_size = 227
folder_path = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataProccesing/"
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg'))]

def prepare_image(file):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: No se pudo leer la imagen {file}")
        return None

    img = cv2.resize(img, (img_size, img_size))
    img = img / 255.0  # Normalizar la imagen
    return img.reshape(-1, img_size, img_size, 1)

model = load_model("C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataTraining/Fotos_Cracks/Concrete_Cracks_Classification_model.h5")

# Iterar a través de cada imagen
for image_file in image_files:
     # Construir la ruta completa de la imagen
    image_path = os.path.join(folder_path, image_file)
    # Preparar la imagen
    img = prepare_image(image_path)
    
    # Construir la ruta completa de la imagen
    #image_path = os.path.join(folder_path, image_file)
    # Verificar si la imagen se leyó correctamente
    #image_data = prepare_image(img_to_predict)

    if img  is not None:
        prediction = model.predict(img)

        # Obtener la categoría predicha
        predicted_class = np.argmax(prediction)

        # Asociar el resultado con las categorías definidas
        categories = ["No color", "Moderate", "Major"]
        confidence = prediction[0][predicted_class] * 100
        pred_text = "Networks prediction: {} Confidence: {:.2f}%".format(categories[predicted_class], confidence)

        # Mostrar la imagen con la predicción
        original_image = cv2.imread(image_path)
        plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))  # Ajuste el canal de color aquí
        plt.axis('off')
        plt.text(0.5, 1.05, pred_text, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=10, color='black', fontweight='bold')

        #plt.show()

    # Detectar contornos
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Definir el color con transparencia (último valor en la tupla BGR)
    alpha_transparency = 0.3  # 60% de transparencia
    transparent_color = (0, 165, 255, int(alpha_transparency * 255)) if categories[predicted_class] == "Moderate" else (0, 0, 255, int(alpha_transparency * 255))

    # Dibuja los contornos en la imagen original
    if categories[predicted_class] == "Moderate":
        cv2.drawContours(original_image, contours, -1, (0, 165, 255), 2)  # Naranja

        # Rellena la zona interna con un patrón de rayas diagonales en naranja tenue
        for cnt in contours:
            cv2.fillPoly(original_image, [cnt], color=transparent_color)
            cv2.polylines(original_image, [cnt], isClosed=True, color=(0, 0, 0), thickness=1)

    elif categories[predicted_class] == "Major":
        cv2.drawContours(original_image, contours, -1, (0, 0, 255), 2)  # Rojo

        # Rellena la zona interna con un patrón de rayas diagonales en rojo tenue
        for cnt in contours:
            cv2.fillPoly(original_image, [cnt], color=transparent_color)
            cv2.polylines(original_image, [cnt], isClosed=True, color=(0, 0, 0), thickness=1)

    #plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGRA2RGBA))  # Ajuste el canal de color aquí también
    #plt.show()
    print (categories[predicted_class]," - Nivel de confidencia: ", confidence,"\n")

    # Guarda la imagen coloreada
    colored_image_path = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataProccesingCracks/colored_image.jpg"
    cv2.imwrite(colored_image_path, original_image)

    # Se crea un folder y se añaden las imágenes coloreadas
    import os
    folder = "images2"
    os.makedirs(folder, exist_ok=True)

    # Guardar la imagen coloreada
    colored_image_path = f"C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataProccesingCracks/{os.path.splitext(image_file)[0]}_colored.jpg"
    cv2.imwrite(colored_image_path, original_image)

    # Muestra la imagen coloreada
    #plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGRA2RGBA))
    #plt.show()
