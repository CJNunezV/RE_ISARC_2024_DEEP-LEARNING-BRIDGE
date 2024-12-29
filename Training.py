import cv2
import numpy as np
import os
import random
import h5py

data_directory = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataTraining/Fotos_Cracks"
img_size = 227
categories = ["No color","Moderate", "Major"] 
training_data = []

def create_training_data():
    for category in categories:
        path = os.path.join(data_directory, category)
        class_num = categories.index(category)

        # read and resize the images and append to training_data a list with the image itself and its class number
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (img_size, img_size))
            training_data.append([new_array, class_num])

######################################################
create_training_data()
random.shuffle(training_data)

X_data = []
y = []

# create X with the features (the images) and y with the targets (labels)
for features, label in training_data:
    X_data.append(features)
    y.append(label)

# reshape the image to be on the correct format for tensorflow (nº images, width, height, channels)
X = np.array(X_data).reshape(len(X_data), img_size, img_size, 1)
hf = h5py.File("C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataTraining/Fotos_Cracks/concrete_Cracks_image_data.h5", "w")#Replace the dots with the directory you want to save your dataset in
hf.create_dataset("X_concrete", data=X, compression="gzip")
hf.create_dataset("y_concrete", data=y, compression="gzip")
hf.close()
######################################################TRAINING
#%tensorflow_version 1.x
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.utils import to_categorical
import numpy as np
import h5py
import cv2

img_size = 227
path = ("C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataTraining/Fotos_Cracks/concrete_Cracks_image_data.h5")
hf = h5py.File(path,'r')

X = np.array(hf.get('X_concrete'))
y = np.array(hf.get("y_concrete"))
hf.close()

X = np.array([cv2.resize(img, (img_size, img_size)) for img in X])
X = X / 255
y = to_categorical(y, num_classes=3)

model = Sequential()

model.add(Conv2D(16, (3, 3), activation="relu", input_shape=(img_size, img_size, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(Flatten())


# Capa de salida para clasificación multiclase (3 categorías)
model.add(Dense(3, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X, y, batch_size=64, epochs=30, validation_split=0.2)

# Guardar el modelo
model.save("C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataTraining/Fotos_Cracks/Concrete_Cracks_Classification_model.h5")
