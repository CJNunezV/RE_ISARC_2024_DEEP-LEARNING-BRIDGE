import os

# Ruta de la carpeta que contiene los archivos a renombrar
folder_path = "C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/Data2"

# Obtener la lista de archivos en la carpeta
files = os.listdir(folder_path)

# Iterar a través de cada archivo
for file_name in files:
    # Construir la ruta completa del archivo actual
    current_path = os.path.join(folder_path, file_name)

    # Obtener el nuevo nombre de archivo eliminando los primeros 5 caracteres
    new_name = file_name[8:]

    # Construir la ruta completa del nuevo archivo
    new_path = os.path.join(folder_path, new_name)

    # Renombrar el archivo
    os.rename(current_path, new_path)

print("Archivos renombrados exitosamente.")