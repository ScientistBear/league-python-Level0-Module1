# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

from tkinter import *
import tkinter as tk
import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    bob = turtle.Turtle()

    radius = simpledialog.askinteger(title='e', prompt='radius plz')
    area = math.pi * radius
    circumference = math.pi * 2 * radius
    yeno = simpledialog.askstring(title='e', prompt='would you like to calculate the area or circumference of the circle')


    if yeno == 'area':
        bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 8, 'normal'))
    elif yeno == 'circumference':
        bob.write(arg="circumference = " + str(circumference), move=True, align='left', font=('Arial', 8, 'normal'))
    bob.forward(10000)
