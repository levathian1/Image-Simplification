#if png convert image to rgb
from tkinter import *
from PIL import Image, ImageOps

nb_col = 5

img = Image.open('cat.jpg').convert("RGB")






def show_res():
    print("hello")
    res = sel()
    res.show()


    
root = Tk()

v = StringVar()

e1 = Entry(root)
e1.insert("1", 5)
label = Label(root)
label.pack()

def nb_colours():
    return int(e1.get())

def sel():
    selected = "Vous avez sélectionné : " + v.get()
    if (v.get() == 'c'):
        #nbColours = int(input("Enter the number of colours you would like to use "))
        result = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=nb_colours())
    elif(v.get() == 'g'):
        print("hi")
        result = ImageOps.grayscale(img)
    return result


v.set("") # initialiser
r1 = Radiobutton(root, text="Color", variable=v, value="c", command=sel)
r1.pack()
r2 = Radiobutton(root, text="Greyscale", variable=v, value="g", command=sel)
r2.pack()
e1.pack()



root.title("Image Simplification")

B = Button(root, text ="Display Image", command=show_res)

B.pack()


root.mainloop()
res = sel()
res.save("result.png")