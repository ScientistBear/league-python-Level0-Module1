import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle

    bob = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='', prompt='what shape do you want')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'square':
        for i in range(4):
            bob.forward(100)
            bob.left(90)
    elif shape == 'circle':
        bob.circle(100)
    elif shape == 'rectangle':
        for i in range(2):
            bob.forward(100)
            bob.left(90)
            bob.forward(200)
            bob.left(90)
    # Call the turtle .done() method
