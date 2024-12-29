import cv2
import numpy as np

# Lee la imagen
path="C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/Bridge/1.jpg"
imagen = cv2.imread(path)

# Convierte la imagen a escala de grises
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplica una umbralización adaptativa para resaltar los bordes de las grietas
th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Encuentra los contornos en la imagen umbralizada
contornos, jerarquia = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibuja los contornos en la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

# Muestra la imagen con los contornos
cv2.imshow('Imagen con contornos', imagen)
cv2.imshow('gray image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
