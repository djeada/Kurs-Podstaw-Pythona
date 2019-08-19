import tkinter

root = tkinter.Tk()
root.geometry('480x480')


def robot():
    print('Jestem robotem')

menu = tkinter.Menu()
root.config(menu=menu)

subMenu = tkinter.Menu(menu)
menu.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='New Project',command=robot)
subMenu.add_command(label='HELP',command=robot)
subMenu.add_separator()
subMenu.add_command(label='New Project',command=robot)

editMenu = tkinter.Menu(menu)
menu.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='New Project',command=robot)
editMenu.add_command(label='HELP',command=robot)
editMenu.add_separator()
editMenu.add_command(label='New Project',command=robot)




root.mainloop()
