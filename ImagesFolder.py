import os
import shutil

# Rutas de entrada y salida
input_folder_path = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataResizedFinal'
output_folder_path = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassificationFinal'

# Crear la carpeta de salida si no existe
os.makedirs(output_folder_path, exist_ok=True)

# Obtener la lista de nombres de archivo en la carpeta de entrada y ordenarla alfanuméricamente
file_names = sorted(os.listdir(input_folder_path))

# Número total de carpetas deseadas
total_folders = 89

# Número de imágenes por carpeta
images_per_folder = len(file_names) // total_folders

# Crear carpetas y copiar imágenes
current_folder_count = 0
for i in range(0, len(file_names), images_per_folder):
    current_folder_count += 1
    folder_name = file_names[i][:8]  # Tomar los primeros 8 caracteres del nombre de la primera imagen
    folder_path = os.path.join(output_folder_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Copiar las imágenes a la carpeta actual
    for j in range(images_per_folder):
        source_path = os.path.join(input_folder_path, file_names[i + j])
        destination_path = os.path.join(folder_path, file_names[i + j])
        shutil.copyfile(source_path, destination_path)
