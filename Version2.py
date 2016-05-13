import Tkinter, tkFont 
'''import sys
import random
import timeit 
import time
import pickle '''

root = Tkinter.Tk()
root.title('Apocalyptic City')

canvas = Tkinter.Canvas(root, height = 300, width = 1000, relief = Tkinter.RAISED, bg= 'black')
canvas.grid()

#checkbox = canvas.create_rectangle( 100, 200, 200, 300, dash = [1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fill = 'green', width = 20)
message = canvas.create_text(380, 250, text = '"Welcome "', fill = 'red', font = ('Arial', -100))

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
    message = canvas.create_text(380, 250, text = '"Welcome "', fill = 'red', font = ('Arial', -100))

    button = Tkinter.Button(root2, text= 'East', width = 10, height = 5, command = newWindow)
    button.grid(row = 2, column= 4)

    button = Tkinter.Button(root2, text= 'South', width = 10, height = 5, command = newWindow)
    button.grid(row = 3, column= 4)

    button = Tkinter.Button(root2, text= 'West', width = 10, height = 5, command = newWindow)
    button.grid(row = 4, column= 4)

    button = Tkinter.Button(root2, text= 'QUIT', width = 10, height = 5, command = newWindow)
    button.grid(row = 5, column= 4)

    
#BUTTONS "LOCATIONS"
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