import tkinter

root = tkinter.Tk()
root.geometry("480x480")

tkinter.Label(root, text="Login").grid(row=0, column=0, padx=2, pady=2)
tkinter.Entry(root).grid(row=0, column=1)

tkinter.Label(root, text="Haslo").grid(row=1, column=0, padx=2, pady=2)
tkinter.Entry(root).grid(row=1, column=1)

tkinter.Button(root, text="Wyslij").grid(row=2)

root.mainloop()
