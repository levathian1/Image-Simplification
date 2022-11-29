#if png convert image to rgb
from tkinter import *
from PIL import Image, ImageOps



img = Image.open('cat.jpg').convert("RGB")


def sel():
    selected = "Vous avez sélectionné : " + v.get()
    label.config(text = selected)
    if (v.get() == 'c'):
        #nbColours = int(input("Enter the number of colours you would like to use "))
        result = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=10)
    elif(v.get() == 'g'):
        print("hi")
        result = ImageOps.grayscale(img)
    return result

def show_res():
    print("hello")
    res = sel()
    res.show()


    
root = Tk()

v = StringVar()
v.set("") # initialiser
r1 = Radiobutton(root, text="Color", variable=v, value="c", command=sel)
r1.pack()
r2 = Radiobutton(root, text="Greyscale", variable=v, value="g", command=sel)
r2.pack()
label = Label(root)
label.pack()



root.title("Image Simplification")

B = Button(root, text ="Display Image", command=show_res)

B.pack()


root.mainloop()
res = sel()
res.save("result.png")