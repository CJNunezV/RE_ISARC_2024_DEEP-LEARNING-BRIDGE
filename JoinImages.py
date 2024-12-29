import os
import cv2

# Ruta de la carpeta que contiene las carpetas con imágenes
base_folder_path = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassificationFinal'

# Obtener la lista de carpetas en la carpeta base
subfolders = sorted([f.path for f in os.scandir(base_folder_path) if f.is_dir()])

# Definir la función de clave alfanumérica para ordenar las carpetas
def alphanum_key(s):
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# Recorrer cada carpeta
for folder_path in subfolders:
    # Obtener la lista de nombres de archivo en la carpeta
    file_names = sorted(os.listdir(folder_path), key=alphanum_key)
    images = [cv2.imread(os.path.join(folder_path, img_file)) for img_file in file_names]

    num_rows = 17
    num_cols = 25

    im_list_2d = [images[i:i+num_cols] for i in range(0, len(images), num_cols)]

    def concat_tile(im_list_2d):
        return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

    # Concatenar las imágenes y guardar la imagen resultante
    im_tile = concat_tile(im_list_2d)
    desired_size = (5472, 3648)

    # Redimensionar la imagen
    im_tile_resized = cv2.resize(im_tile, desired_size)

    # Obtener el nombre del archivo de la primera imagen
    first_image_name = file_names[0][:8]

    # Guardar la imagen redimensionada con el nombre de la primera imagen
    output_path = os.path.join(base_folder_path, f'{first_image_name}.jpg')
    cv2.imwrite(output_path, im_tile_resized)

print("Proceso completado.")