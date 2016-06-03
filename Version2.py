# -*- coding: utf-8 -*-
import Tkinter, tkFont 

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
photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
canvas.create_image(0,0, image = photo)
canvas2 = Tkinter.Canvas(root, height = 300, width = 900, relief = Tkinter.RAISED, bg = 'red')
canvas2.grid()

#----------------------------------------------------------------------------------INTRO---------------------------------------------------------------------------------------------------------------------------

message = canvas.create_text(380, 90, text = 'Welcome to Apocalyptic City!', fill = 'white', font = ('Toxico', -40))
message2 = canvas2.create_text(470, 140, text = 'Your objective in this game will be to\nget out of the building to saftey to\na certain destination.\n', fill = 'black', font = ('True Lies', -40))


times_pressed =0

def pressed(x):
    
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += x
    #recreates the text box
    customFont = tkFont.Font(family = 'Serif', size = 40)
    editor = Tkinter.Text(width = 25, height =4, font =(customFont))
    editor.grid(row = 0, column = 0) 
    
    #adds the text to the box
    editor.insert(Tkinter.END, " Number of puppies killed: ")
    editor.insert(Tkinter.END, times_pressed)
    editor.see(Tkinter.END)
    
    #disable chrging the text box
    editor.config(state = Tkinter.DISABLE)
    #editor.config(state = Tkinter.NORMAL)

#-------------------------------------------------WRONG WAY--------------------------------------------------------------------- 

def wrong_way():
    root5 = Tkinter.Tk()
    root5.title('WRONG WAY')
    
    canvas = Tkinter.Canvas(root5, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    
    message = canvas.create_text(300, 100, text = ' You can\'t go that way!',fill = 'red', font = ('Yu Gothic', -50))
    print message 
    
#---------------------------------------------------OFFICE------------------------------------------------------------  
  
def newWindow():
    #global message
    root2 = Tkinter.Tk()
    root2.title('Room: Office')
    
    canvas = Tkinter.Canvas(root2, height = 100, width = 990, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root2, height = 390, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message1 = canvas.create_text(100, 60, text = 'Room: Office', fill = 'white', font = ('Yu Gothic', -30))
    print message1  
    message = canvas2.create_text(400, 200, text = 'Papers are shattered everywhere. The lights\nare flashing on and off. Next to you is a\nblue paper.\n\nIt reads: *Escape to the labatory hidden under\nan old facotry building.It should be located a\ncouple of blocks west of where you are located.*\n\nHead north or east', fill = 'black', font = ('Yu Gothic', -30))
    print message 
    
    button = Tkinter.Button(root2, text= 'North', width = 10, height = 5, command = con_room)
    button.grid(row = 1, column= 4)
    

    button = Tkinter.Button(root2, text= 'East', width = 10, height = 5, command = desk)
    button.grid(row = 1, column= 5)

    button = Tkinter.Button(root2, text= 'South', width = 10, height = 5, command = wrong_way)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root2, text= 'West', width = 10, height = 5, command = wrong_way)
    button.grid(row = 3, column= 5)

    button = Tkinter.Button(root2, text= 'QUIT', width = 10, height = 5, command = root2.destroy)
    button.grid(row = 5, column= 4)
    
#---------------------------------------------------------INTRO------------------------------------------------------------------  
#START OF THE GAME 

button = Tkinter.Button(root, text= 'START GAME', width = 10, height = 5, command = newWindow)
button.grid(row = 0, column= 1)

button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root.destroy)
button.grid(row = 0, column= 2)

#------------------------------------------------------------ELEVATOR/NORTH---------------------------------------------------------------------- 

def con_room():    
    root3 = Tkinter.Tk()
    root3.title('Room: Conference Room')
    editor3 = Tkinter.Text(master = root3, width= 45, height = 0)
    editor3.grid( row= 0 , column = 0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor3.insert(Tkinter.END,"add?")
    editor3.see(Tkinter.END)
    
    canvas = Tkinter.Canvas(root3, height = 100, width = 990, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    canvas2 = Tkinter.Canvas(root3, height = 390, width = 990, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    
    message = canvas.create_text (200, 60, text = 'Room: Conference Room', fill = 'white', font = ('Yu Gothic', -30))
    print message
    message1 = canvas2.create_text(1000, 100, text = 'You are now standing in the Conference Room. Decomposing bodies are laying ageround. The smell of rotting human flesh is making you sick. There\'s a flashlight on the table. Pick it up...you might need it later on.\n\nTo add an item type in...\n\n>add\nor\n>no\n\n\nTo view at any time your inventory just type "inventory"\n\nAfter head "east"', fill = 'black', font = ('Yu Gothic', -30))
    print message1 
    
    
    if editor3 == "add":
        addToInventory(input)
        print(inventory)
    print 
    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root3, text= 'North', width = 10, height = 5, command = newWindow3)
    button.grid(row = 0, column= 5)
    
    button = Tkinter.Button(root3, text= 'East', width = 10, height = 5, command = elevator)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root3, text= 'South', width = 10, height = 5, command = newWindow3)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root3, text= 'West', width = 10, height = 5, command = wrong_way)
    button.grid(row = 2, column= 3)

    button = Tkinter.Button(root3, text= 'QUIT', width = 10, height = 5, command = root3.destroy3)
    button.grid(row = 5, column= 4)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def desk():    
    root6 = Tkinter.Tk()
    editor6 = Tkinter.Text(master = root6, width = 45, height = 0)
    editor6.grid(row = 0, colum =0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor6.insert(Tkinter.End, "Room : Elevator")
    editor6.see(Tkinter.End)
    
    canvas = Tkinter.Canvas(root6, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    #photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
    #canvas.create_image(0,0, image = photo)
    canvas2 = Tkinter.Canvas(root6, height = 350, width = 500, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message = canvas2.create_text(300, 100, text = 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', fill = 'green', font = ('Yu Gothic', -50))
    print message 


    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root6, text= 'North', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)
    
    button = Tkinter.Button(root6, text= 'East', width = 10, height = 5, command = newWindow)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root6, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root6, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 2, column= 3)

    button = Tkinter.Button(root6, text= 'QUIT', width = 10, height = 5, command = root6.destroy)
    button.grid(row = 5, column= 4)

def newWindow3():    
    root4 = Tkinter.Tk()
    editor4 = Tkinter.Text(master = root4, width = 45, height = 0)
    editor4.grid(row = 0, colum =0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor4.insert(Tkinter.End, "Room : Elevator")
    editor4.see(Tkinter.End)
    
    canvas = Tkinter.Canvas(root4, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    #photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
    #canvas.create_image(0,0, image = photo)
    canvas2 = Tkinter.Canvas(root4, height = 350, width = 500, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
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
    
def elevator():    
    root4 = Tkinter.Tk()
    editor4 = Tkinter.Text(master = root4, width = 45, height = 0)
    editor4.grid(row = 0, colum =0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor4.insert(Tkinter.End, "Room : Elevator")
    editor4.see(Tkinter.End)
    
    canvas = Tkinter.Canvas(root4, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    #photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
    #canvas.create_image(0,0, image = photo)
    canvas2 = Tkinter.Canvas(root4, height = 350, width = 500, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
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


