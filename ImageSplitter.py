import cv2
import math
import os
from PIL import Image
from split_image import split_image
##############################################################################################################
#path='C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/djiphotos/v2.jpg'
#image=227x227

#image=cv2.imread(path)
#y=image.shape[0] #length in first dimension
#x=image.shape[1] #length in second dimension
#columns=math.ceil(x/227)
#rows=math.ceil(y/227)
#x=227*columns
#y=227*rows
#print(x,y)

#resized = cv2.resize(image, (x,y), interpolation = cv2.INTER_AREA)
#cv2.imwrite('C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/djiphotos/resized.jpg', resized)
###############################################################################################################

#split_image('C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/djiphotos/resized.jpg',rows,columns, False, ['C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/djiphotos'])

data_directory = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassification"
output_directory = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/Data2"

for img_name in os.listdir(data_directory):
    img_path = os.path.join(data_directory, img_name)

    # Cargar la imagen usando OpenCV
    img = cv2.imread(img_path)

    # Verificar si la imagen se cargó correctamente
    if img is not None:
        # Obtener las dimensiones de la imagen
        y, x, _ = img.shape
        columns=math.ceil(x/227)
        rows=math.ceil(y/227)
        x=227*columns
        y=227*rows
        resized = cv2.resize(img, (x, y), interpolation=cv2.INTER_AREA)
        # Escribir la imagen redimensionada en el directorio de salida
        output_path = os.path.join(output_directory, f"resized_{img_name}")
        cv2.imwrite(output_path, resized)
        # Cortar la imagen redimensionada y guardar los fragmentos
        split_image(output_path, rows, columns, False, [output_directory])


