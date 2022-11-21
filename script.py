#if png convert image to rgb
from PIL import Image, ImageOps

img = Image.open('cat.jpg').convert("RGB")

grayscale = input("Grayscale or not (g or c)")

if (grayscale == 'c'):
    nbColours = int(input("Enter the number of colours you would like to use "))
    result = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=nbColours)
else:
    result = ImageOps.grayscale(img)
    
result.show()
result.save("result.png")