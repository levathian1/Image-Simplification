#if png convert image to rgb
from PIL import Image

img = Image.open('cat.jpg').convert("RGB")
nbColours = int(input("Enter the number of colours you would like to use "))
result = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=nbColours)
result.show()
result.save("result.png")