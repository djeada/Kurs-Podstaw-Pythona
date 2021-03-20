import tkinter

root = tkinter.Tk()
root.geometry("480x480")

l = tkinter.Label(root, text="Aplikacja")
l.pack()


def funkcjaPrzycisku():
    print("Wcisnieto przycisk")


b = tkinter.Button(
    root,
    text="Jestem Przyciskiem1",
    width=10,
    bg="red",
    fg="white",
    command=funkcjaPrzycisku,
)
b.pack(side=tkinter.RIGHT)
b2 = tkinter.Button(root, text="Jestem Przyciskiem2", command=funkcjaPrzycisku)
b2.pack(side=tkinter.BOTTOM)
b3 = tkinter.Button(root, text="Jestem Przyciskiem3", command=funkcjaPrzycisku)
b3.place(x=380, y=0)

root.mainloop()
