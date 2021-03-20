import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("480x480")

zdjecie = Image.open("znany_model.jpg")
zdjecie = zdjecie.resize((150, 100), Image.ANTIALIAS)
ikonka = ImageTk.PhotoImage(zdjecie)
tkinter.Label(root, image=ikonka).pack()

canvas = tkinter.Canvas(root, width=300, height=300, bg="blue")
canvas.pack()
canvas.create_image(30, 15, anchor=tkinter.SW, image=ikonka)

root.mainloop()
