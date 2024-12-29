###https://github.com/kennethleungty/Image-Metadata-Exif/tree/main
#########################################################################1. Environemnt Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import cv2
from exif import Image
################################################################################## 2. Getting a photo
folder_path = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassification'
img_filename = 'DJI_0428.jpg'
img_path = f'{folder_path}/{img_filename}'
with open(img_path, 'rb') as img_file:
    img = Image(img_file)
print(img.has_exif)

# List all EXIF tags contained in the image
sorted(img.list_all())

# 3. Getting all data
print("\n ALL DATA:\n")
def get_metadata_single(img_path):
    with open(img_path, 'rb') as img_file:
        img = Image(img_file)
        if not img.has_exif:
            print('Image does not have EXIF metadata')
        else:
            df = pd.DataFrame(columns=['attribute', 'value'])
            attr_list = img.list_all()
            
            # Add image file name
            df = pd.concat([df, pd.DataFrame([{'attribute': 'image_path', 'value': img_path}])], ignore_index=True)

            for attr in attr_list:
                value = img.get(attr)
                dict_i = {'attribute': attr,'value': value}
                df = pd.concat([df, pd.DataFrame([dict_i])], ignore_index=True)
            
            df.sort_values(by='attribute', inplace=True)
            df.set_index('attribute', inplace=True)
            return df
metadata_df = get_metadata_single(img_path)
# Configurar pandas para mostrar todas las columnas y filas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

attribute_interest = ['_exif_ifd_pointer', '_gps_ifd_pointer', 'aperture_value', 'max_aperture_value', 'compressed_bits_per_pixel', 'compression', 'datetime', 'datetime_digitized', 'datetime_original', 'exposure_program', 'exposure_time', 'f_number', 'focal_length', 'focal_length_in_35mm_film', 'gps_altitude', 'gps_altitude_ref', 'gps_latitude', 'gps_latitude_ref', 'gps_longitude', 'gps_longitude_ref', 'gps_version_id', 'light_source', 'max_aperture_value', 'metering_mode', 'orientation', 'photographic_sensitivity', 'shutter_speed_value', 'x_resolution', 'y_and_c_positioning', 'y_resolution']

values_attribute = [metadata_df.loc[atributo].values[0] for atributo in attribute_interest if atributo in metadata_df.index]
# Imprimir el DataFrame
print(metadata_df)
print(metadata_df.loc['gps_altitude'].values[0])
print("\n",values_attribute)

###################################
# 4.Modify Metadata
#(i) Add attribute
#We can also assign new attributes even if the attribute is not already present in the existing image.
#Attributes that can be added must be based on the exif.Image attributes available. See this link for the list of all the EXIF tags: https://exif.readthedocs.io/en/latest/api_reference.html#image-attributes
from exif import Image as ExifImage

print("\n NOW I'M UPDATING INFORMATION")
folder_path = 'C:/Users/CHRISTOPHER/Desktop/AlgTesis/ISARC2024/DataClassification2'
img_path= f'{folder_path}/{img_filename}'


with open(img_path, 'rb') as img_file:
    img = Image(img_file)
# Add new attribute
#img.exif_ifd_pointer = values_attribute[0]
#img._gps_ifd_pointer = values_attribute[1]
img.aperture_value = values_attribute[2]
img.max_aperture_value = values_attribute[3]
#img.compressed_bits_per_pixel = values_attribute[4]
#img.compression = values_attribute[5]
#img.exposure_program = values_attribute[9]
#img.exposure_time = values_attribute[10]
img.f_number = values_attribute[11]
img.focal_length = values_attribute[12]
img.focal_length_in_35mm_film = values_attribute[13]
img.gps_altitude = values_attribute[14]
img.gps_altitude_ref = values_attribute[15]
img.gps_latitude = values_attribute[16]
img.gps_latitude_ref = values_attribute[17]
img.gps_longitude = values_attribute[18]
img.gps_longitude_ref = values_attribute[19]
img.gps_version_id = values_attribute[20]
img.light_source = values_attribute[21]
img.max_aperture_value = values_attribute[22]
img.metering_mode = values_attribute[23]
img.orientation = values_attribute[24]
img.photographic_sensitivity = values_attribute[25]
img.shutter_speed_value = values_attribute[26]
#img.x_resolution = values_attribute[27]
#img.y_and_c_positioning = values_attribute[28]
#img.y_resolution = values_attribute[29]

# Check updated metadata
print(f'exif_ifd_pointer: {img.get("exif_ifd_pointer")}')

# Write image with modified EXIF metadata to an image file
with open(f'{folder_path}/modified_{img_filename}', 'wb') as new_image_file:
        new_image_file.write(img.get_file())