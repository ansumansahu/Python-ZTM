from email.mime import image
from PIL import Image

img=Image.open('./Pokedex/pikachu.jpg')
print(img.format)
print(img.size)
print(img.mode)

from PIL import ImageFilter
#we have some filter options to modify our image
filter_img=img.filter(ImageFilter.SHARPEN) 

filter_img.save("pika_filter.png","png") 
#png format supports these image filters, jpg may give errors
#name and format

#we can also use convert image to diff formats
convert_img=img.convert('L') #L-greyscale
convert_img.save("pika_convert.png","png")

#just shows the file
# convert_img.show()

#rotate image
rot=img.rotate(90)
rot.save("pika_rotate.png","png")

#resize image
res=img.resize((300,300))
#takes tuple input so double bracks needed
res.save('pika_thumbnail.png','png')
#but resize may modify image aspect ratio if initial image is not proportional
#So instead use img.thumbnail(()) which retains aspect ratio 
#thumbnail max range is (400,400)

# crop - box=(x,x,x,x) then 
# image_name.crop(box) , box has corner values
