import tkinter

root = tkinter.Tk()
root.geometry('480x480')

def funkcjaPrzycisku1():
    print('Wcisnieto Przycisk1')

def lewy(event):
    print('Na przycisk2 kliknieto lewym przyciskim myszy')

def prawy(event):
    print('Na przycisk2 kliknieto prawym przyciskim myszy')

def funkcjaPrzycisku3(event):
    print('Wcisnieto Przycisk3')

def funkcjaOkna(event):
    print('Kliknieto na okienko')

b1 = tkinter.Button(root,text='Przycisk1',command=funkcjaPrzycisku1)
b1.pack()

b2 = tkinter.Button(root,text='Przycisk2')
b2.bind('<Button-1>',lewy)
b2.bind('<Button-3>',prawy)
b2.pack()

b3 = tkinter.Button(root,text='Przycisk3')
b3.bind('<Button-3>',funkcjaPrzycisku3)
b3.pack()

root.bind('<Button-3>',funkcjaOkna)

root.mainloop()
