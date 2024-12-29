import os
from exif import Image as ExifImage

# Rutas de las carpetas que contienen las imágenes
folder_path_original = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassification'
folder_path_modified = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassification2'

# Obtener la lista de nombres de archivo en ambas carpetas
file_names_original = sorted(os.listdir(folder_path_original))
file_names_modified = sorted(os.listdir(folder_path_modified))
# Definir atributos de interés
attribute_interest = ['_exif_ifd_pointer', '_gps_ifd_pointer', 'aperture_value', 'max_aperture_value',
                       'f_number', 'focal_length', 'focal_length_in_35mm_film', 'gps_altitude',
                       'gps_altitude_ref', 'gps_latitude', 'gps_latitude_ref', 'gps_longitude',
                       'gps_longitude_ref', 'gps_version_id', 'light_source', 'max_aperture_value',
                       'metering_mode', 'orientation', 'photographic_sensitivity', 'shutter_speed_value']


# Iterar sobre cada par de imágenes correspondientes
for file_name_original, file_name_modified in zip(file_names_original, file_names_modified):
    # Crear la ruta completa para cada imagen
    img_path_original = os.path.join(folder_path_original, file_name_original)
    img_path_modified = os.path.join(folder_path_modified, file_name_modified)

    # Abrir las imágenes y obtener los valores de atributo de interés
    with open(img_path_original, 'rb') as img_file_original, open(img_path_modified, 'rb') as img_file_modified:
        img_original = ExifImage(img_file_original)
        img_modified = ExifImage(img_file_modified)

        # Obtener valores de atributo de la imagen original
        values_attribute = [img_original.get(atributo) for atributo in attribute_interest if atributo in img_original.list_all()]

        # Aplicar los valores de atributo a la imagen modificada
        img_modified.aperture_value = values_attribute[2]
        img_modified.max_aperture_value = values_attribute[3]
        img_modified.f_number = values_attribute[11]
        img_modified.focal_length = values_attribute[12]
        img_modified.focal_length_in_35mm_film = values_attribute[13]
        img_modified.gps_altitude = values_attribute[14]
        img_modified.gps_altitude_ref = values_attribute[15]
        img_modified.gps_latitude = values_attribute[16]
        img_modified.gps_latitude_ref = values_attribute[17]
        img_modified.gps_longitude = values_attribute[18]
        img_modified.gps_longitude_ref = values_attribute[19]
        img_modified.gps_version_id = values_attribute[20]
        img_modified.light_source = values_attribute[21]
        img_modified.max_aperture_value = values_attribute[22]
        img_modified.metering_mode = values_attribute[23]
        img_modified.orientation = values_attribute[24]
        img_modified.photographic_sensitivity = values_attribute[25]
        img_modified.shutter_speed_value = values_attribute[26]

        # Escribir la imagen con metadatos modificados a un nuevo archivo
        new_image_path = os.path.join(folder_path_modified, f'modified_{file_name_modified}')
        with open(new_image_path, 'wb') as new_image_file:
            new_image_file.write(img_modified.get_file())

print("Proceso completado.")