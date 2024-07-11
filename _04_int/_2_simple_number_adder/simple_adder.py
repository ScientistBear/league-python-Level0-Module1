"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""


import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':

    window = Tk()

    window.withdraw()

    numb_one = simpledialog.askstring(title='e', prompt='number one')

    numb_two = simpledialog.askstring(title='e',prompt='number two')

    messagebox.showinfo(message=numb_one + numb_two)










