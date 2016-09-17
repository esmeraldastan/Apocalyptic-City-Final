# -*- coding: utf-8 -*-
import Tkinter, tkFont 
from Tkinter import *


import sys
import random
import timeit 
import time
import pickle

root = Tkinter.Tk()
root.title('Apocalyptic City')



#INVENTORY
inventory = []

#INVENTORY
def addToInventory(item):
    item = raw_input('> what do you want to add?? ')
    inventory.append(item)
    


canvas = Tkinter.Canvas(root, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
canvas.grid()
canvas2 = Tkinter.Canvas(root, height = 300, width = 900, relief = Tkinter.RAISED, bg = 'red')
canvas2.grid()
photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
canvas.create_image(0,0, image = photo)

#----------------------------------------------------------------------------------INTRO---------------------------------------------------------------------------------------------------------------------------

message = canvas.create_text(380, 90, text = 'Welcome to Apocalyptic City!', fill = 'white', font = ('Toxico', -40))
message2 = canvas2.create_text(470, 140, text = 'Your objective in this game will be to\nget out of the building to saftey to\na certain destination.\n', fill = 'black', font = ('True Lies', -40))



#-------------------------------------------------WRONG WAY--------------------------------------------------------------------- 

def wrong_way():
    root = Tkinter.Tk()
    root.title('WRONG WAY')
    
    canvas = Tkinter.Canvas(root, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    
    message = canvas.create_text(300, 100, text = ' You can\'t go that way!',fill = 'red', font = ('Yu Gothic', -50))
    print message 
    
#---------------------------------------------------OFFICE------------------------------------------------------------  
#2

def newWindow():
    #global message
    root = Tkinter.Tk()
    root.title('Room: Office')
    
    canvas = Tkinter.Canvas(root, height = 100, width = 990, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root, height = 390, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message1 = canvas.create_text(300, 60, text = 'Room: Office', fill = 'white', font = ('Yu Gothic', -30))
    print message1  
    message = canvas2.create_text(400, 200, text = 'Papers are shattered everywhere. The lights\nare flashing on and off. Next to you is a\nblue paper.\n\nIt reads: *Escape to the labatory hidden under\nan old facotry building.It should be located a\ncouple of blocks west of where you are located.*\n\nHead north or east', fill = 'black', font = ('Yu Gothic', -30))
    print message 
    
    button = Tkinter.Button(root, text= 'North', width = 10, height = 5, command = con_room)
    button.grid(row = 1, column= 4)
    
    button = Tkinter.Button(root, text= 'East', width = 10, height = 5, command = desk)
    button.grid(row = 1, column= 5)

    button = Tkinter.Button(root, text= 'South', width = 10, height = 5, command = wrong_way)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root, text= 'West', width = 10, height = 5, command = wrong_way)
    button.grid(row = 3, column= 5)

    button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root1.destroy)
    button.grid(row = 1, column= 6)
    
#---------------------------------------------------------INTRO------------------------------------------------------------------  
#START OF THE GAME 

button = Tkinter.Button(root, text= 'START GAME', width = 10, height = 5, command = newWindow)
button.grid(row = 0, column= 1)

button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root.destroy)
button.grid(row = 0, column= 2)

#------------------------------------------------------------CON./NORTH---------------------------------------------------------------------- 
#3

def con_room():    
    root = Tkinter.Tk()
    root.title('Room: Conference Room')
    editor = Tkinter.Text(master = root, width= 45, height = 0)
    editor.grid( row= 0 , column = 0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor.insert(Tkinter.END,"add?")
    editor.see(Tkinter.END)
    
    canvas = Tkinter.Canvas(root, height = 100, width = 990, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root, height = 400, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    
    message = canvas.create_text (200, 60, text = 'Room: Conference Room', fill = 'white', font = ('Yu Gothic', -30))
    print message
    message1 = canvas2.create_text(500, 200, text = 'You are now standing in the Conference Room. Decomposing\nbodies are laying ageround. The smell of rotting human flesh is\nmaking you sick. There\'s a flashlight on the table. Pick it up...you\nmight need it later on.\n\nTo add an item type in...\n\n>add\n\nAfter head "east"', fill = 'black', font = ('Yu Gothic', -30))
    print message1 
    
    
    if editor == "add":
        addToInventory(input)
        print(inventory)
    print 
    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root, text= 'North', width = 10, height = 5, command = wrong_way)
    button.grid(row = 2, column= 3)
    
    button = Tkinter.Button(root, text= 'East', width = 10, height = 5, command = elevator)
    button.grid(row = 2, column= 6)

    button = Tkinter.Button(root, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 3)

    button = Tkinter.Button(root, text= 'West', width = 10, height = 5, command = wrong_way)
    button.grid(row = 3, column= 6)

    button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root2.destroy)
    button.grid(row = 5, column= 4)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def desk():    
    root = Tkinter.Tk()
    root.title('Location: Secutary Desk')
    
    
    canvas = Tkinter.Canvas(root, height = 100, width = 990, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root, height = 350, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    

    
    message = canvas.create_text(300, 60, text = 'Location: Secutrary Desk', fill = 'white', font = ('Yu Gothic', -30))
    print message
    message2 = canvas2.create_text(450, 150, text = 'You are standing next to your securary\'s desk. A "flashlight"\nstands on top. Pick it up you might need it later on.\n\nType\n>add\n\nAfter head either "north" to the elevator or "east" to the stairs.', fill = 'black', font = ('Yu Gothic', -30))
    print message2 


    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root, text= 'North', width = 10, height = 5, command = elevator)
    button.grid(row = 0, column= 4)
    
    button = Tkinter.Button(root, text= 'East', width = 10, height = 5, command = stairs)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root, text= 'South', width = 10, height = 5, command = wrong_way)
    button.grid(row = 1, column= 4)

    button = Tkinter.Button(root, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 1, column= 3)

    button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root3.destroy)
    button.grid(row = 5, column= 4)
    
#---------------------------------------------------------------------------------------------------------------------------------------------
def stairs():    
    root = Tkinter.Tk()
    root.title("Location: Stairs")

    canvas = Tkinter.Canvas(root, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root, height = 350, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
     
    message = canvas2.create_text(300, 100, text = 'Location: Stairs', fill = 'green', font = ('Yu Gothic', -50))
    print message 
 
    message2 = canvas2.create_text(300, 100, text = 'You need to restore to full health.There is a green serum laying on the ground. \n\nType "restore".\n\nThis will get you to full health.\nAfter head "down".', fill = 'green', font = ('Yu Gothic', -50))
    print message2 


    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root, text= 'North', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)
    
    button = Tkinter.Button(root, text= 'East', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 2, column= 3)

    button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root4.destroy)
    button.grid(row = 5, column= 4)   
    
def elevator():    
    root = Tkinter.Tk()
    root.title("Location: Elevator")

    canvas = Tkinter.Canvas(root, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root, height = 350, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message= canvas.create_text
    message = canvas2.create_text(300, 100, text = 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', fill = 'green', font = ('Yu Gothic', -50))
    print message 


    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root4, text= 'North', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)
    
    button = Tkinter.Button(root4, text= 'East', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root4, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root4, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 2, column= 3)

    button = Tkinter.Button(root4, text= 'QUIT', width = 10, height = 5, command = root4.destroy)
    button.grid(row = 5, column= 4)
    
root.mainloop()


