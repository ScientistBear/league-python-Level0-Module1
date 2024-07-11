"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    numb1 = simpledialog.askinteger(title='', prompt='number one')

    numb2 = simpledialog.askinteger(title='', prompt='number two')

    opp = simpledialog.askstring(title='opp', prompt='pick a operation(use +, *, /, -)')

    if opp == '+':
        messagebox.showinfo(message=numb1+numb2)

    if opp == '*':
        messagebox.showinfo(message=numb1*numb2)

    if opp == '/':
        messagebox.showinfo(message=numb1/numb2)

    if opp == '-':
        messagebox.showinfo(message=numb1-numb2)

