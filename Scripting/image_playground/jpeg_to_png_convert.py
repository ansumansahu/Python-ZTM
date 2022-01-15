from email.mime import image
import sys
import os
from tkinter import image_names
from PIL import ImageFilter,Image

image_path=sys.argv[1]
new_path=sys.argv[2]

if os.path.exists(new_path)==False:
    os.makedirs(new_path)

for item in os.listdir(image_path):
    img = Image.open(f'{image_path}{item}')
    image_name=os.path.splitext(item)[0]
    #seperates name and extension into two parts

    img.save(f'{new_path}/{image_name}.png','png')