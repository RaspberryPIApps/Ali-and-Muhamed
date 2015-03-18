from Tkinter import *
from turtle import *
from Tkinter import Tk, Canvas, Frame, BOTH
from random import  seed, randint
import random
import math
from swampy.TurtleWorld import* 

# building the appropriate GUI that contains 3 buttons, the first one will plot the exaxt polygon,
# the second one plots the approximate, and the third button is the exit button

class App:
   
    def __init__(gui, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Enter the number of sides').grid(row=0, column=0)
        Label(frame, text='Note:The number must be more than 3').grid(row=1, column=0)
        gui.ang_var = IntVar()
        Entry(frame, textvariable=gui.ang_var).grid(row=0, column=1)
        Label(frame, text='Enter the Length of the side').grid(row=0, column=4)
        Label(frame, text='Note:The length must be larger than 50').grid(row=1, column=4)
        gui.chord_var = IntVar()
        Entry(frame,  textvariable=gui.chord_var).grid(row=0, column=5)
        Label(frame, text='Notifications').grid(row=3, column=0)
        gui.result_var =  StringVar()  
        Label(frame, textvariable=gui.result_var).grid(row=3, column=1)
        button = Button(frame, text='Plot the perfect polygon', command=gui.draw)
        button.grid(row=4,  column=0)
        button = Button(frame, text= 'Plot the erroneous polygon', command=gui.erroneous)
        button.grid(row=4, column =3)
        button = Button(frame, text='Exit', command=gui.exit)
        button.grid(row=4,  column=5)
        
        

    def convert(gui):
        c = gui.c_var.get()
        gui.result_var.set(gui.t_conv.convert(c))
        
# defining a function that draws the polygon, after converting the unser-entered numbers into global variables         

    def draw(gui):
    
        global angle
        global length
        global n

        n = gui.ang_var.get()
        length = gui.chord_var.get()


        if n <4 or n> 50:
            gui.result_var.set("The number of sides must be more than 3, please change the number")

        elif length <50 or length >200:
            gui.result_var.set("The length of each side much be larger than 50, please change the number")

        else:
            print (n)
            print (length)
            
            
            def polygon(t):
                global n
                global length
                anglee = 360.0/n
                for i in range(n):
                    print(int(t.get_x()), int(t.get_y()))
                    fd(t, length)
                    lt(t, anglee)
            world = TurtleWorld()
            bob= Turtle()
            print bob
            polygon (bob)
            wait_for_user()    
            
 # defining the erroneous function which plots the approximate polygon after the user has entered the correct numbers       
        
        
    def erroneous(gui):
        global angle
        global length
        global n
        
        n = gui.ang_var.get()
        length = gui.chord_var.get()
        
        if n <4 or n> 50:
            gui.result_var.set("The number of sides must be more than 3, please change the number")
            
        elif length <50 or length >200:
            gui.result_var.set("The length of each side much be larger than 50, please change the number")
            
        else:
            print(n)
            print(length)
            
            
            
            def hexagon(t):
                global n
                global length
                anglee = 360.0/n
                for i in range(n):
                    print(int(t.get_x()), int(t.get_y()))
                    side = random.randint(72,120)
                    ang = random.randint(50,70)
                    fd(t, side)
                    lt(t, ang)
            world = TurtleWorld()
            bob= Turtle()
            print bob
            hexagon (bob)
            wait_for_user()           
            




    def exit(gui):
        root.quit()

   
root = Tk()
root.wm_title('FAU Robot polygon')
app = App(root)
root.mainloop()