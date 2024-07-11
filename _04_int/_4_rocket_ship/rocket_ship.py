from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()


# This code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # This defines the x and y coordinated of all three points
    canvas.create_oval(x - 150, y - -100, x + 150, y + 400, fill='red', width=0)
    canvas.create_oval(x - 100, y - -100, x + 100, y + 300, fill='orange', width=0)
    canvas.create_oval(x - 50, y - -100, x + 50, y + 200, fill='yellow', width=0)

    # of a triangle
    points = [x, y, x - 50, y + 100, x + 50, y + 100]
    canvas.create_polygon(points, fill='gray', width=2)  # draws triangle
    
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.

    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    

# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
