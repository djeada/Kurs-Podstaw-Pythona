import tkinter

root = tkinter.Tk()
root.geometry('480x480')

c = tkinter.Canvas(root, height=300, width=350, bg='green')
c.pack()

for i in range(5):
    c.create_line(0,30*i,350,30*i, width=10)

c.create_oval(30,30, 150, 150, fill='red')
c.create_rectangle(20,200, 150, 300, fill='blue')

root.mainloop()
