# -*- coding: utf-8 -*-
import sys
import random
import time
 

#INVENTORY
inventory = []

#TIMER
sec = 0 

#Into to the game 
time.sleep(0.5)
print "Welcome to Apocalyptic City!\n"
print "Your objective in this game will be to get out of\nthe building to saftey at a certain destination.\n"
print
print 'For instructions at any time just type in "instructions".'
print 
print "----"


node = None 

#INVENTORY
def addToInventory(item):
    item = raw_input('> what do you want to add?? ')
    inventory.append(item)
    
#-----------------------------------------------------------------------------------------------------------------------------

#CHARACTERS
#player status 
class player(object):
    
    def __init__(self, health = 49800, attack = 500):
        self.attack = attack 
        self.health = health 
        
        
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
    def damage(self, amount):
        self.health -= amount
        
me = player() 

       
#HP OF ZOMBIE
class Zombie(object):
    def __init__(self, health = 5000, attack = 1500):
        self.health = health
        self.attack = attack 
        

    #COMMAND TO ATTACK     
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
    #DAMAGE TAKEN   
    def damage(self, amount):
        self.health -= amount
        
zombie = Zombie()

#second zombie
class Zombie2(object):
    def __init__(self, health = 6000, attack = 1500):
        self.health = health
        self.attack = attack 
        

    #COMMAND TO ATTACK     
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
    #DAMAGE TAKEN   
    def damage(self, amount):
        self.health -= amount
        
zombie2 = Zombie2()
             
 #HP OF INFECTED
class Infected(object):
    def __init__(self, health = 6000, attack = 500):
        self.health  = health 
        self.attack = attack 
        
    #COMMAND ATTACK 
    def attacks(self, target):
        target.damage(self. attack)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
    #DAMAGE TAKEN         
    def damage(self, amount):
        self.health -= amount 
        
        
infected = Infected() 

class Infected2(object):
    def __init__(self, health = 7000, attack = 1000):
        self.health  = health 
        self.attack = attack 
        
    #COMMAND ATTACK 
    def attacks(self, target):
        target.damage(self. attack)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
    #DAMAGE TAKEN         
    def damage(self, amount):
        self.health -= amount 
        
        
infected2 = Infected2() 
#-------------------------------------------------------------------------------------------------------------             
        
#ITEMS     
class Item(object):
    def __init__(self, name):
        self.name = name
        

#WEAPONS AT USE
#SUPERCLASS                
class Weapons(Item):
    
    def __init__(self, name, damage, weight):
        super(Weapons, self).__init__(name)
        self.damage = damage
        self.weight = weight
         
#SUB_CLASSES        
class two_hand(Weapons):
    def __init__(self, name, damage = 100, weight = 150):
        super(two_hand, self).__init__(name, damage = 100, weight = 150)
        
    def cut_off(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
sword = two_hand(Weapons) 
      
        
class two_hand2(Weapons):
    def __init__(self, name, damage = 50, weight = 80):
        super(two_hand2, self).__init__(name, damage = 50, weight = 80)
        
    def slaughter(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
axe = two_hand2(Weapons)
        
class two_hand3(Weapons):
    def __init__(self, name, damage = 55, weight = 100):
        super(two_hand3, self).__init__(name, damage = 55, weight = 100)
        
    def shoot(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
cross_bow = two_hand3(Weapons)
        
    
class one_hand(Weapons):
    def __init__(self, name, damage = 10, weight = 15):
        super(one_hand, self).__init__(name, damage = 10, weight = 15)
        
    def stab(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
        
dagger = one_hand(Weapons)

class one_hand2(Weapons):
    def __init__(self, name, damage = 20, weight = 0):
        super(one_hand2, self).__init__(name, damage = 20, weight = 0)
        
    def hit(self, target):
        target.damage(self.damage)
        if target.health <= 0 :
            return "0"
        else:
            return target.health
            
club = one_hand2(Weapons)
    

                
#CONSUMABLES   
class Consumable(Item):
    
    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health
        
class health_potion(Consumable):
    def __init__(self, name, health = 200):
        super(health_potion, self).__init__(name, health = 200)
        
a = health_potion(Consumable)  
b = player()  



#--------------------------------------------------------------------------------------------------------------------def save():
 
#start of the map         
class Building:
    
    def __init__(self, name, description, up, down, north, east, south, west, right, left, outside, inside):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.right = right
        self.left = left
        self.outside = outside 
        self.inside = inside 
        
    def move(self, direction):
        global node 
        node = globals()[getattr(self, direction)]
        
print 'You have woken up from an unconscious hit in the head. The last thing you remember was escaping the white gas that was spreading throughout the city.' 
print
                   
#BUILDING

#THIRD FLOOR            
Office = Building("Office", 'Papers are shattered everywhere. The lights are flashing on and off. Next to you is a blue paper.\n\nType in "pick up" to read what it says.', None, None, 'Conference', 'Secutary', None, None, None, None, None, None)
Conference = Building("Conference Room", 'You are now standing in the Conference Room. Decomposing bodies are laying around. The smell of rotting human flesh is making you sick. There\'s a flashlight on the table. Pick it up...you might need it later on.\n\nTo add an item type in...\n\n>add\nor\n>no\n\n\nTo view at any time your inventory just type "inventory"\n\nAfter head "east"', None, None, None, 'Elevator', 'Office',None, None, None, None, None)
Elevator = Building("Elevator", 'You need to restore to full health.There is a green serum laying on the ground. \n\nType "restore".\n\nThis will get you to full health.\nAfter head "down".', None, 'Elevator2', None, None, 'Secutary Desk',None, None, None, None, None)
Stairs = Building("Stairs", 'The walls are coverd with blood. You are not alone. Zombies and infecteds run the area now. You don\'t want to encounter with one ...it can be your end.To go down the stairs type in "down" to go on to the next floor.There is blood covering the walls….Bodies laying down with body parts missing. Be careful..\n\nIf you want info on these creatures type in "creatures"', None, 'Stairs1', None, None, None,None, None, None, None, None)
Secutary = Building("Secutary Desk",' You are standing next to your securary\'s desk. A flash light stands on top. Pick it up you might need it later on.\n/nType\n>add\nor\n>no\n\nAfter head either "north" to the elevator or "east" to the stairs.', None, None, 'Elevator', 'Stairs', None , None, None, None, None, None)

#PATH TO SECOND FLOOR
Stairs1 = Building("Stairs", 'Pieces from the ceiling are blocking your path. Find another path to get out.\n\nHead "west"', None, None, None, None, None,'Office1', None, None, None, None)
Elevator2 = Building("Second Floor", 'You are now on the second floor. A loud growl is coming for the stairs.... an infected is charging towards you.\n\nHead "south".', 'Elevator', None, None, None, 'Office1', None , None, None, None, None)

#SECOND FLOOR
Office1 = Building('Office 1', 'There seems nothing to be in here to help you defeat the infected.\nHead "west" into the other room. There might be something in there.', None, None, 'Elevator2', None, None , 'Office2', None, None, None, None)
Office2 = Building('Office 2 ', 'Huh, nothing in here as well. The infecteds are coming in closer.\nKeep heading "west"', None, None, None, None , None, 'Janitor', None, None, None, None)
Janitor= Building('Janitor Room', 'Cleaning applicances are scattered everywhere. Within the room there is another door.\n\nWEAPONS\n\nit reads.Type "inside" to get in.', None, None, None, 'Office1', 'Secret',None, None, None, None, 'Secret')
Secret = Building('Secret Door', 'Great you made it in. Take a step "north"', None, None, 'Weapon', 'Janitor', None,None, None, None, None, None)
Weapon = Building('Weapon Room', 'A variety of weapons are displayed. Take the ones that you think will be useful. Remember thought there is a limit of 3 weapons you can take.To see how to you your weapons type "attack instructions".\nType in..\n>add\n\n..to exit and head out Type "east".', None, None, None, 'Elevator3', 'Secret',None, None, None, None, None)
Bathroom = Building('Restroom', 'The smell of rottening meat is rising in here. Place the first bomb in here. ', None, None, None, None, 'Stairs','Elevator', None, None, None, None)

#PATH TO FIRST FLOOR
Stairs2 = Building('Stairs', 'Head down as quick and possible', None, 'Lobby', None, None, None, None, None, None, None, None)
Elevator3 = Building('Elevator', 'Head "down"', None, 'Lobby', None, None, None, None, None, None, None, None)

#FIRST FLOOR
Lobby = Building('Lobby', 'You are now in the first floor. Head "east"', None, None, None, 'Center', None, None, None, None, None, None)
Center = Building('Center', 'There is a bomb here. Head "outside" quick!', None, None, None, None, None, None, None, None, 'Enterence', None)

#OUTSIDE
Enterence=Building('Enterence', 'BOOM!!!Pieces of glass shattering everywhere. Bodies flying in the sky. Luckly you have made it out saftely. It won\'t be easy now to make it you your destination with infecteds and zombies around.\n\nHead "south".', None, None, None, None, 'Coffee',None, None, None, None, None)
Coffee = Building('Coffee Shop', 'You are now standing infront of a coffee shop. If you are low on health head "inside" to restore to full health. If not continue..\nHead "west"\n\n To check on status of health type "health".', None, None, None, None, None,None, None, None, None, 'Enterance2')
Enterance2 = Building('Inside', 'You are now inside the coffee shop. There is a table to your "right" with health serum. Head towards it.', None, None, None, None, None, None,'Table', None, None, None)
Table = Building('Table','Type in "restore" to recover to full health. Then head "outside".', None, None, None, None, None, None, None, None, 'Coffee2', None)
Coffee2 = Building('Enterance', 'Okay you are now outside. Head "west".', None, None, None, None, None, 'Bank', None, None, None, None)
Bank =Building('Bank', 'You are passing by a bank. Across for it is a Gift Shop. It\'s starting to get dark. Something is coming twords you. Type in "flashlight" to see what it is ', None, None, 'Shop', 'Coffee', None,'Casino', None, None, None, None)
Inside = Building ('Front Desk', 'Infront of you is a key. Its the key the will allow you inside the factory.Head "outside" after you pick up the key.Type "add" to pick up the key...', None, None, None, None, None, None, None, None, None , None)
Shop =Building('Gift Shop', 'You are standing infront of a gift shop. Windows broken and bodies of the dead laying everywhere.Nothing foung to be useful.\nHead "south"', None, None, None, None, 'Bank', None, None, None, None, None)
Casino =Building('Casino', 'As you pass by the casion you noiced how the city had turned into ruins in matter of days.Keep heading "west" you are close', None, None, None, 'Bank', None, 'Bakery', None, None, None, None)
Bakery =Building('Bakery', 'You have made it far.The once sweet smell by bread is replaces by rottning bodies.The old factory is just "west"', None, None, None, 'Casino', None, 'Factory', None, None, None, None)

#DESTINATION

Factory =Building('Factory', 'You have made it to the Factory. Hurry up inside', None, None, None, None, None, None, None, None, None, 'Desk')
Desk =Building('Front Desk', 'Take a look at the paper on the desk. It should give you information on where to find the lab.', None, None, None, None, None, None, None, None, 'Factory', None)
Production =Building('Production Room', 'You have entered the production room. There to the "west" of you is a door opening.', None, None, None, None, None, None, None, None, None, None)
Pressure =Building('Pressure Room', 'The elevator to the lab is just infront of you. Head on you are almost there', None, 'Labitory', None, None, None, None, None, None, None, None)
Labitory =Building('Labatory', 'Congradulations you have made it to the Lab!', 'Pressure', None, None, None, None, None, None, None, None, None)



node = Office

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#RUN THROUGH THE MAP 
while True:
    print "Room: " + node.name
    print 
    print "Description: " + node.description 
#------------------------------------------------------------------------------------------------------------------------------------------------
    
    #WORD DEFINE
    define = ['creatures']
    restore = ['restore']
    response = ['up', 'down', 'north', 'east', 'south', 'west', 'right', 'left', 'outside', 'inside'] 
    pick = ['pick up']
    

    
    command = raw_input('>').strip().lower()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------
     
    #QUITE THE PROGRAM 
    if command in ['q', 'exit', 'quit']:
        sys.exit(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------    
    #DEFINATION ON WORDS    
    if command in define:
        print '''
                Infected- A person who had been contaminated by the gas.
                Zombie- A dead person risen from the dead.The chemicals within\nthe gas had an effect on the dead making them come back to life.
    
             '''
    if command == "instructions":
        print '''
        
        Directions:                To add an item      
        *north                     Type "add"          
        *east                                          
        *south                                         
        *west                                          
        *down                                           
        *up                                             
        *inside
        *outside
            '''    
            
    if command == " attack instructions":
        print '''
        
        attack = for basic attack
        hit = attack with club
        stab = attack with dagger
        shoot = attack with cross bow
        slaughter = attack with axe 
        cut off = attack with sword '''
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    if command == "zombie health":
        print zombie.health
        
    if command == "infected health":
        print infected.health
        
                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------             
    #SEE INSIDE INVENTORY         
    if command == "inventory":
        print (inventory)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------
#BLUE PAPER        
    #paper read out 
    if command in pick:
        print
        print '*Escape to the labatory hidden under an old facotry building.It should be located a couple of blocks west of where you are located.*'
        print 
        print 'Head either "north" or "east"'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    #MOVE INTO DIFFERNT ROOMS 
    if command in response:
        try:
           node.move(command)
        except:
            print 'You can\'t do that way!'
            
           #print 'You can\'t do that way!  
        #except:
           # pass
           
#-------------------------------------------------------------------------------------------------------------------------------
           
    #RESTORE HEALTH       
    if command == 'restore':
        new_health = a.health + b.health
        print new_health,'full health restored'
        
#-------------------------------------------------------------------------------------------------------------------------        

    #INVENTORY FOR ITEMS/WEAPONS
        
    if command == "add":
        addToInventory(input)
        print (inventory)
    print

#-------------------------------------------------------------------------------------------------------------------------------

    if node == Weapon:
        print '''
                    Weapons Available:
            
                    *axe
                    *sword
                    *cross bow
                    *dagger
                    *club
                    
                '''


            
    #INFO OF WEAPONS        
    if command == "axe damage":
        print axe.damage 
    elif command == "sword damage":
        print sword.damage
    elif command == "cross bow damage":
        print cross_bow.damage
    elif command == "dagger damage":
        print dagger.damage
        
    if command == "axe weight":
        print axe.weight
    elif command == "sword weight":
        print sword.weight
    elif command == "cross bow weight":
        print cross_bow.weight
    elif command == "dagger weight":
        print dagger.weight

 #-----------------------------------------------------------------------------------------------------------
 
     # PRINT OUT HEALTH THROUGHOUT THE GAME   
    if command == "health":
        print me.health
        
#--------------------------------------------------------------------------------------------------------------        
    # door 
    if node == Secret :
        print "Figure out the passcode to get inside!"

        password = "3546", "5515", "1651", "4539", "4620" #passwords to open up the doors 
        wordIndex = random.randint(0,len(password)-1)
        code_rip = password[wordIndex]
        user_guesses = ''
        turns = 10 #the player will have only 10 times to try to figure out the code


        while turns > 0:
            left = 0
            for number in code_rip:
                if number in user_guesses:
                    print number,
                else:
                    print "#",
                    left += 1
            if left == 0:
                    print
                    print
                    print "Excellent, move on."# move into the next room 
                    
                    break
            
            print 
            
            guess = raw_input("Guess the four Numbers:")

            user_guesses += guess 
            if guess not in code_rip:
                    turns -=1
                    print "Sorry number not in the secret code. \n\n Please try again"
                    print "You have", +turns, 'left'
            if turns == 0:
                    print "Sorry you lose"#change
                    
                    
                    
#--------------------------------------------------------------------------------------------------------------------------------------------

                    
    if node == Elevator2:
        print 'There is an infected infront of you...attack it. Type "attack".'
        
        while me.health > 0:
            command = raw_input('>')
            if command == "attack":
                me.health -= infected.attack
                print "Your health is now", me.health
                print "Your attacked your enemy for", me.attacks(infected),"damage"
                
            if infected.health <= 0:
                print 
                print
                print"Great, you have defeated the zombie!!!\n"
                
                break
            print
            
        
        
            if infected.health <=0:
                print
                print
                print "Great you have defeated the infected!!!\n"
        
                break
        
            print 
    
            if me.health <= 0:
                print "sorry you died"  
                sys.exit(0)                  
#------------------------------------------------------------------------------------------------------------------------------
#ZOMBIE ATTACK    
    
    if node == Stairs1:
        print 'There is a zombie infront of you. Type "attack".'
        
                
        while me.health > 0:
            command = raw_input('>')
            if command == "attack":
                me.health -= zombie.attack 
                print "Your health is now", me.health 
                print "You attacked your enemy for", me.attacks(zombie),"damage"
        

        
            if zombie.health <= 0:
                print
                print
                print "Great, you have defeated the zombie!!!\n"
        
                break
        
            print 
    
            if me.health <= 0:
        
                print "Sorry, you died."
                sys.exit(0)        
#-------------------------------------------------------------------------------------------------------------------- 

    if node == Bank:
        print 'There is a infected infront of you attack it. Use your weapons.'
        
        while me.health > 0:
                command = raw_input('>')
                if command == "stab":# use of dagger
                    me.health -= infected2.attacks 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", dagger.stab(infected2),"damage."
                elif command == "attack":# basic attack
                    me.health -= infected2.attacks 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", me.attacks(infected2),"damage."
                elif command == "shoot":#use of cross bow
                    me.health -= infected2.attacks 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", cross_bow.shoot(infected2),"damage."     
                elif command == "cut off":#use of sword
                    me.health -= infected2.attacks 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", sword.cut_off(infected2),"damage."
                elif command == "slaughter":#use of axe
                    me.health -= infected2.attacks 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", axe.slaughter(infected2),"damage."

            
                if infected.health <= 0:
                    print
                    print
                    print "Great, you have defeated the zombie"
        
                    break
        
                print 
    
                if me.health <= 0:
        
                    print "Sorry, you died."
                    sys.exit(0)

       
'''    if node == Bank:
        print 'There is a infected infront of you attack it. Type "attack".'
        
        while me.health > 0:
                command = raw_input('>')
                if command == "stab":# use of dagger
                    me.health -= infected.attack 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", dagger.stab(infected),"damage."
                elif command == "attack":# basic attack
                    me.health -= infected.attack 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", me.attacks(infected),"damage."
                elif command == "shoot":#use of cross bow
                    me.health -= infected.attack 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", cross_bow.shoot(infected),"damage."     
                elif command == "cut off":#use of sword
                    me.health -= infected.attack 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", sword.cut_off(infected),"damage."
                elif command == "slaughter":#use of axe
                    me.health -= infected.attack 
                    print "Your health is now", me.health 
                    print "You attacked your enemy for", axe.slaughter(infected),"damage."

            
                if infected.health <= 0:
                    print
                    print
                    print "Great, you have defeated the zombie"
        
                    break
        
                print 
    
                if me.health <= 0:
        
                    print "Sorry, you died."
                    break'''
            
                                        
#not done yet


        