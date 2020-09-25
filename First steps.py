#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This notebook is only here for training purposes.


# In[2]:


#Slicing : select portions of a variable
Example = "Slicing"
Example[1:3]


# In[3]:


#Stride : select a portion of a variable with a certain pace
print(Example[::2])
print(len(Example)) #How many characters
Example[2:7:3] #every third element from the 2nd to the last


# In[4]:


#Concatenation
print(Example * 3)
print(Example + " is not striding")


# In[5]:


#Escape sequences
print("My Example may be too long to print \nso I'm cutting it somewhere in the middle") #next line
print("I want \t this \t far away") #tab
print("Here's a back slash \\") #include a back slash


# In[6]:


#Upper, Lower, replace, find
print(Example.upper())
print(Example.lower())
replacement = Example.replace("i", "o") #what we want to change / what will replace it
print(replacement)
Example.find("ici") #finds the index of the first character


# In[7]:


#Lists, subsetting, operations
manga_chapters = [["Dragon Ball / Z", 519],
                  ["Shingeki no Kyojin", 130],
                  ["One Piece", 984],
                  ["Bleach", 686],
                  ["Naruto", 700],
                  ["Berserk", 357],
                  ["FMA", 108]]
print(manga_chapters[3][0]) # name [0] of the fourth element [3] in the list
print(manga_chapters[-2]) # penultimate element in the list

#Let's simplify this
MC = list(manga_chapters) #We don't want a name with the same reference but a clear copy

print(MC[2][0], "has way more chapters than",MC[-1][0],(MC[2][1], MC[-1][1]))


# In[8]:


#Adding chapters that have no relation whatsoever, just for the sake of training
print(MC[5][1] + MC[-3][1], 'chapters in total')
print(MC[3] + MC[2])

#Slicing
Shōnen = MC[2:] + MC[0]
Shōnen

#Replace
MC[1] = "Seven Deadly Sins", 346
print(MC)


# In[9]:


#Sort, append & extend
random1 = [13, 48, 17, 95, 29]
random2 = [83, 20, 47, 30, 10]
random12 = list(random1 + random2)

print(sorted(random12, reverse = True)) #descending order
print("Before extend, there are ", len(random12), "elements")

random12.extend([22, 2, 2]) #adding 3 elements (integers)
print("After extend, there are ",
      len(random12), "elements")

random12.append([22, 2, 2]) #adding one element (a list)
print("After append, there are ",
      len(random12), "elements")

print(random12[-1]) ; print(random12[-4])


# In[10]:


#Intro to methods with .reverse()
Books = [["A Song of Ice and Fire"],
        ["The Malazan Book of the Fallen"],
        ["The Stormlight Archive"],
        ["Harry Potter"],
        ["CHERUB"]]

print(Books)
Books.reverse() ; print(Books)


# In[11]:


#Tuples (= lists but inmutable)
Tuple = (3, (4,37), 94, (23, 48, 29)) #Nesting
print(Tuple[0]) ; print(Tuple[1]) ; print(Tuple[3][1])


# In[30]:


#Sets, set(), Inter / Union, difference(), add()
Set1 = {"A", 3, (1,2), 2.9}
Set2 = set(Tuple)

Set12Int = Set1 & Set2 #This works as well : Set1.intersection(Set2)
print("This is the common element between the two sets :", Set12Int)
print("These are the unique elements contained in Set 2 :", Set2.difference(Set1))

Set12 = Set1.union(Set2) #the integer 3 is not duplicated
Set12.add("WhatIsThis")
Set12

#set(set).issubset to find out if set is a subset


# In[38]:


#Dictionnaries, keys(), values()
Larousse = {"Get" : 1, "The" : 9, "Joke" : 0, "?" : 5}

print(Larousse["Get"]) #We want to know the value of the first key
print("I'm sure you did :", Larousse.keys())
print("Here are the values associated :", Larousse.values())
Larousse["WhyAreWeHere"] = "JustToSuffer"
Larousse


# In[ ]:




