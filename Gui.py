import tkinter

root = tkinter.Tk()
root.geometry('480x480')

l = tkinter.Label(root, text='bibo')
l.pack()

def buttonFunction():
    print('Hello world!')

b = tkinter.Button(root, text='Duplo', command=buttonFunction)
b.place(x=0,y=0)

root.mainloop()









