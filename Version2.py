# -*- coding: utf-8 -*-
import Tkinter, tkFont 

import sys
import random
import timeit 
import time
import pickle

root = Tkinter.Tk()
root.title('Apocalyptic City')





        
#THIRD FLOOR            
#Office = Building("Office", 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', None, None, 'Conference', 'Secutary', None, None, None, None, None, None)
#Conference = Building("Conference Room", 'You are now standing in the Conference Room. Decomposing bodies are laying around. The smell of rotting human flesh is making you sick. There\'s a flashlight on the table. Pick it up...you might need it later on.\n\nTo add an item type in...\n\n>add\nor\n>no\n\n\nTo view at any time your inventory just type "inventory"\n\nAfter head "east"', None, None, None, 'Elevator', 'Office',None, None, None, None, None)
#Elevator = Building("Elevator", 'You need to restore to full health.There is a green serum laying on the ground. \n\nType "restore".\n\nThis will get you to full health.\nAfter head "down".', None, 'Elevator2', None, None, 'Secutary Desk',None, None, None, None, None)
#Stairs = Building("Stairs", 'The walls are coverd with blood. You are not alone. Zombies and infecteds run the area now. You don\'t want to encounter with one ...it can be your end.To go down the stairs type in "down" to go on to the next floor.There is blood covering the walls….Bodies laying down with body parts missing. Be careful..\n\n If you want info on these creatures type in "creatures"', None, 'Stairs1', None, None, None,None, None, None, None, None)
#Secutary = Building("Secutary Desk",' You are standing next to your securary\'s desk. A flash light stands on top. Pick it up you might need it later on.\nType\n>add\nor\n>no\nAfter head either "north" to the elevator or "east" to the stairs.', None, None, 'Elevator', 'Stairs', None , None, None, None, None, None)

#node = Office        
        

canvas = Tkinter.Canvas(root, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
canvas.grid()
#photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
#canvas.create_image(0,0, image = photo)
canvas2 = Tkinter.Canvas(root, height = 350, width = 900, relief = Tkinter.RAISED, bg = 'red')
canvas2.grid()



#checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
message = canvas.create_text(380, 90, text = 'Welcome to Apocalyptic City!', fill = 'white', font = ('Yu Gothic', -50))
message2 = canvas2.create_text(480, 150, text = 'Your objective in this game will be to get out of\nthe building to saftey at a certain destination.\n', fill = 'black', font = ('Yu Gothic', -50))
#380,250
#######################
#Checkbox
#####################

#box = Tkinter.Checkbutton(root, text='This is a checkbot.')
#box.grid(row=1, column=0)

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
    
def newWindow():
    #global message
    root2 = Tkinter.Tk()
    editor2 = Tkinter.Text(master = root2, width= 45, height = 0)
    editor2.grid( row= 0 , column = 0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor2.insert(Tkinter.END,"Room : Office")
    editor2.see(Tkinter.END)
    
    canvas = Tkinter.Canvas(root2, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    #photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
    #canvas.create_image(0,0, image = photo)
    canvas2 = Tkinter.Canvas(root2, height = 350, width = 500, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message = canvas2.create_text(300, 100, text = 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', fill = 'green', font = ('Yu Gothic', -50))
    print message 



    #checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
    #check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
    #message = canvas.create_text(380, 90, text = 'Welcome to Apocalyptic City!', fill = 'white', font = ('Yu Gothic', -50))
    #message2 = canvas2.create_text(480, 150, text = 'Start the game', fill = 'black', font = ('Yu Gothic', -50))
    #380,250
    #######################

    
    button = Tkinter.Button(root2, text= 'North', width = 10, height = 5, command = newWindow2)
    button.grid(row = 1, column= 4)
    

    button = Tkinter.Button(root2, text= 'East', width = 10, height = 5, command = newWindow2)
    button.grid(row = 2, column= 5)

    button = Tkinter.Button(root2, text= 'South', width = 10, height = 5, command = newWindow2)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root2, text= 'West', width = 10, height = 5, command = newWindow2)
    button.grid(row = 4, column= 4)

    button = Tkinter.Button(root2, text= 'QUIT', width = 10, height = 5, command = root2.destroy)
    button.grid(row = 5, column= 4)
    

#START OF THE GAME 
button = Tkinter.Button(root, text= 'START GAME', width = 10, height = 5, command = newWindow)
button.grid(row = 0, column= 1)

button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = root.destroy)
button.grid(row = 0, column= 2)


def newWindow2():    
    root3 = Tkinter.Tk()
    editor3 = Tkinter.Text(master = root3, width = 45, height = 0)
    editor3.grid(row = 0, colum =0, sticky = (Tkinter.N, Tkinter.W, Tkinter.E))
    editor3.insert(Tkinter.End, "Room : Elevator")
    editor3.see(Tkinter.End)
    
    canvas = Tkinter.Canvas(root3, height = 200, width = 900, relief = Tkinter.RAISED, bg= 'black')
    canvas.grid()
    #photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
    #canvas.create_image(0,0, image = photo)
    canvas2 = Tkinter.Canvas(root3, height = 350, width = 500, relief = Tkinter.RAISED, bg = 'red')
    canvas2.grid()
    
    message = canvas2.create_text(300, 100, text = 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', fill = 'green', font = ('Yu Gothic', -50))
    print message 


    
    #BUTTONS "LOCATIONS"

    button = Tkinter.Button(root3, text= 'North', width = 10, height = 5, command = newWindow3)
    button.grid(row = 0, column= 5)
    
    button = Tkinter.Button(root3, text= 'East', width = 10, height = 5, command = newWindow3)
    button.grid(row = 0, column= 5)

    button = Tkinter.Button(root3, text= 'South', width = 10, height = 5, command = newWindow3)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root3, text= 'West', width = 10, height = 5, command = newWindow3)
    button.grid(row = 2, column= 3)

    button = Tkinter.Button(root3, text= 'QUIT', width = 10, height = 5, command = root3.destroy3)
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

    button = Tkinter.Button(root4, text= 'QUIT', width = 10, height = 5, command = root3.destroy)
    button.grid(row = 5, column= 4)
    

root.mainloop()


