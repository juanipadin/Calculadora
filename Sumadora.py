from tkinter import *

def sumar():
    r.set (float(n1.get()) + float(n2.get()))

root = Tk()
root.resizable(0,0)
root.config(bd=15)

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root, text="Número 1").pack()

Entry(root,justify="center",textvariable=n1).pack() #primer número
Label(root, text="Número 2").pack()
Entry(root,justify="center",textvariable=n2).pack() #segundo número

Button (root, text="Sumar", command=sumar).pack()

Label(root, text="Resultado").pack()
Entry(root,justify="center",textvariable=r,state="disable").pack() #resultado



root.mainloop()