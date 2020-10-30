#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This notebook is for training purposes


# In[1]:


#Branching
age = 21

if age >= 21 :
    print("You can enter, " "the Bar is open")
elif age > 18 :
    print("You can enter")
else :
    print("DENIED")


# In[2]:


#Loops

for i in range(0,23):
    print(i, end = " ")


# In[3]:


numbers = [1, 0, 3, 4, 5]

for i, numbers in enumerate(numbers):
    print(i, numbers)


# In[4]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

i = 0
list1 = 0

while(list1 != 7) :
    list1 = numbers[i]
    i = i + 1
    print(list1)


# In[7]:


for index, number in enumerate(numbers):
    print("The index (" + str(index) + ") does not correpond to the number in the list (" + str(number) + ")")
    #str(index +1) if we want to start from 0


# In[5]:


colors = ['blue', 'cyan', 'purple', 'red', 'yellow', 'orange']
i = 0
not_red = []

while(not_red != 'red'):
    not_red = colors[i]
    i = i + 1
    print(not_red)
    
print(i, 'iterations to get red into not_red')


# In[6]:


#Loop with a sublist
Diff_levels = [["I want to live", 1],
              ["Hurt me plenty", 2],
              ["Ultra-violence", 3],
              ["Nightmare", 4],
              ["Ultra-nightmare", 5]]

for x in Diff_levels :
    print("Number " + str(x[1]) + " corresponds to " + x[0] + " difficulty in Doom Eternal")


# In[9]:


Dictionnary = {"Watch Dogs Legion": "October",
              "Assassin's Creed Valhalla": "November",
              "Cyberpunk 2077": "December (or not)"}
for key, value in Dictionnary.items(): #For dictionnaries, the method items() is used
    print(key + " releases in " + value)


# In[7]:


#Functions

def adding(a,b):
    """
    adds a to b
    """
    c = a + b 
    return(c)

adding(3,22)


# In[8]:


def happymeal(a):
    """
    Can you order a Happy Meal ? 
    """
    global not_influenced #Variable available outside of the function
    not_influenced = "I'll eat what I want"
    
    if(a < 13):
        return "Here's your Happy Meal"
    else:
        return "Get a Big Mac"

print(happymeal(9))
print(happymeal(13))
print(not_influenced)


# In[9]:


def Organizer(**arguments):
    for key in arguments:
        print(key + " : " + arguments[key])
        
Organizer(Sony = "Playstation", Microsoft = "Xbox", Nintendo = "Switch")


# In[10]:


#Classes & Methods

class Car(object):  #always start your class definition like this (object as class parent for a start)
    def __init__(self, make, model, color):  #4 attributes within the constructor __init__
        self.make = make;
        self.model = model;
        self.color = color;  # ; are important here
        self.owner_number = 0
    def info(self):   #Methods from here, never forget the (self) by default
        print("Make:", self.make)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Number of owners:", self.owner_number)
    def sell(self):
        self.owner_number = self.owner_number + 1

make = "Honda"
model = "Accord"
color = "Blue"

my_car = Car(make, model, color)
my_car.info()


# In[11]:


my_car2 = Car(color = "Black", make = "Audi", model = "A6") #the order is not important if you assign each attribute
my_car2.info()


# In[13]:


class Mangas(object):
    def __init__(self, name, author, genre, nb_volumes):
        self.name = name;
        self.author = author;
        self.genre = genre;
        self.nb_volumes = nb_volumes
    def info(self):
        print("Name :", self.name)
        print("Author :", self.author)
        print("Genre :", self.genre)
        print("Number of volumes released as of October 2020 :", self.nb_volumes)

OnePiece = Mangas("One Piece", "Eiichirō Oda", "Shônen", 97)
Bleach = Mangas("Bleach", "Tite Kubo", "Shônen", 74)
Berserk = Mangas("Berserk", "Kentaro Miura", "Seinen", 40)

Bleach.info()


# In[15]:


dir(Mangas) #Lists all the methods of a class


# In[ ]:




