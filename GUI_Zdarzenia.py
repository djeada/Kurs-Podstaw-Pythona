import tkinter

root = tkinter.Tk()
root.geometry('480x480')

def funkcjaPrzycisku():
    print('Wcisnieto przycisk', )

def funkcjaZdarzenia(event):
    print('Wcisnieto Zdarzenie')

b = tkinter.Button(root,text='Przycisk1')
b.pack()
b.bind('<Button-1>',funkcjaZdarzenia)


b2 = tkinter.Button(root,text='Przycisk2',command=funkcjaPrzycisku)
b2.pack()

b3 = tkinter.Button(root,text='Przycisk3')

b3.pack()
b3.bind('<Button-3>',funkcjaZdarzenia)


root.bind('<Button-3>',funkcjaZdarzenia)

root.mainloop()
