import tkinter

root = tkinter.Tk()
root.geometry('480x480')

glowneMenu = tkinter.Menu()
root.config(menu=glowneMenu)

fileMenu = tkinter.Menu(glowneMenu)
glowneMenu.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New File')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Open Module')
fileMenu.add_separator()
fileMenu.add_command(label='Recent Files')

editMenu = tkinter.Menu(glowneMenu)
glowneMenu.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Undo')
editMenu.add_command(label='Redo')

podMenu = tkinter.Menu(editMenu)
editMenu.add_cascade(label='Male',menu=podMenu)
podMenu.add_command(label='Undo')
podMenu.add_command(label='Redo')

root.mainloop()
