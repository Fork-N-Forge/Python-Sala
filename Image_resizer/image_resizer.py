from PIL import Image

img = Image.open("Python_gui/images/pixyworld5.jpg")

print(img.width,img.height)
img.show()
# This is for downscaling a image

#img = img.resize((int(img.width/2),int(img.height/2)))

# This is for upscaling a image
img = img.resize((int(img.width*2),int(img.height*2)),resample=Image.LANCZOS)

#lanczos is used to maintain it in highest resolution 

print(img.width,img.height)
img.show()

# Upscaling a part of image so we need its coordinate l,b,w,h

img = img.resize((int(img.width*2),int(img.height*2)),resample=Image.LANCZOS,box=(10,32,60,80))
print(img.width,img.height)
img.show()