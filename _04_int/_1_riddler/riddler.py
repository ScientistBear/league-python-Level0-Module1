"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox, simpledialog, Tk


messagebox.showinfo(title='riddler',message='time for riddles. Are you ready?!')

qone = simpledialog.askstring(title='q1', prompt='What ends in a w but has no end?')

qtwo = simpledialog.askstring(title='q2', prompt='I am four times as old as my daughter. In 20 years time I shall be twice as old as her. How old are we now?')

qthree = simpledialog.askstring(title='q3', prompt='What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? "What is it?"')

if qone == 'A rainbow!' or qone =='a rainbow' or qone =='A rainbow':
    messagebox.showinfo(title='', message='question one was correct')
else:
    messagebox.showinfo(title='', message='question one was incorrect')

if qtwo == 'I am 40 and my daughter is 10.' or qtwo =='I am 40 and my daughter is 10' or qtwo =='i am 40 and my daughter is 10':
    messagebox.showinfo(title='', message='question two was correct')
else:
    messagebox.showinfo(title='', message='question two was incorrect')

if qthree == 'A die (dice)' or qthree =='dice' or qthree =='a die' or qthree =='A die':
    messagebox.showinfo(title='', message='question three was correct')
else:
    messagebox.showinfo(title='', message='question three was incorrect')

