import Tkinter, tkFont 

import sys
import random
import timeit 
import time
import pickle

root = Tkinter.Tk()
root.title('Apocalyptic City')

canvas = Tkinter.Canvas(root, height = 200, width = 1000, relief = Tkinter.RAISED, bg= 'black')
canvas.grid()
photo = Tkinter.PhotoImage(file = "C:\Users\Esmeralda\Pictures\game pic.gif")
canvas.create_image(0,0, image = photo)
canvas2 = Tkinter.Canvas(root, height = 100, width = 1000, relief = Tkinter.RAISED, bg = 'blue')
canvas2.grid()



#checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
message = canvas.create_text(380, 100, text = 'Welcome to Apocalyptic City!', fill = 'white', font = ('Yu Gothic', -50))
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
    editor2.insert(Tkinter.END,"heyyo")
    editor2.see(Tkinter.END)
    
    #BUTTONS "LOCATIONS"
    button = Tkinter.Button(root2, text= 'North', width = 10, height = 5, command = newWindow)
    button.grid(row = 1, column= 4)
    

    button = Tkinter.Button(root2, text= 'East', width = 10, height = 5, command = newWindow)
    button.grid(row = 2, column= 4)

    button = Tkinter.Button(root2, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root2, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 4, column= 4)

    button = Tkinter.Button(root2, text= 'QUIT', width = 10, height = 5, command = root2.destroy)
    button.grid(row = 5, column= 4)

    
#BUTTONS "LOCATIONS"
#navigation form 
#all windows but combat sys.
button = Tkinter.Button(root, text= 'North', width = 10, height = 5, command = newWindow)
button.grid(row = 1, column= 4)

button = Tkinter.Button(root, text= 'East', width = 10, height = 5, command = newWindow)
button.grid(row = 2, column= 4)

button = Tkinter.Button(root, text= 'South', width = 10, height = 5, command = newWindow)
button.grid(row = 3, column= 4)

button = Tkinter.Button(root, text= 'West', width = 10, height = 5, command = newWindow)
button.grid(row = 4, column= 4)

button = Tkinter.Button(root, text= 'QUIT', width = 10, height = 5, command = newWindow)
button.grid(row = 5, column= 4)

root.mainloop()
