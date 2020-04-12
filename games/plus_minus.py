from tkinter import *
from tkinter import ttk

from random import randint as rnd


def example():
    x1 = rnd(0, 30)
    x2 = rnd(0, 30)
    s = x1 + x2
    return x1, x2, s


def check():
    print(result.get())


root = Tk()
root.title('Сложение и вычетание')
root.geometry('400x300')
lbl_1 = ttk.Label(root, text="Введите нужное число").grid(row=3, column=1)
x1, x2, s = example()
lbl_x1 = ttk.Label(root, text=str(x1), font="Arial 34").grid(row=5, column=1, sticky=E)

lbl_plus = Label(root, text='+', font="Arial 34").grid(row=5, column=2)

lbl_x2 = ttk.Label(root, text=str(x2), font="Arial 34").grid(row=5, column=3)

lbl_equil = ttk.Label(root, text='=', font="Arial 34").grid(row=5, column=4)

result = Entry(root, width=3, font="Arial 34").grid(row=5, column=5)

butn1 = ttk.Button(root, text='Check', command=check).grid(row=7, column=3)
root.mainloop()
