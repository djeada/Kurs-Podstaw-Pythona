import tkinter

root = tkinter.Tk()
 
# sticky defines how the widget expands (N, NE, E, SE,
# S, SW, W, NW)
# padx and pady provide padding around the widget above
# and below it

tkinter.Label(root, text=" Name").grid(row=0, sticky=tkinter.W, padx=4)
tkinter.Entry(root).grid(row=0, column=1, sticky=tkinter.W, pady=4)
 
tkinter.Label(root, text="Last Name").grid(row=1, sticky=tkinter.W, padx=4)
tkinter.Entry(root).grid(row=1, column=1, sticky=tkinter.E, pady=4)
 
tkinter.Button(root, text="Submit").grid(row=3)
 
root.mainloop()
