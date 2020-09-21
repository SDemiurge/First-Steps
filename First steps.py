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


# In[75]:


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

#Adding chapters that have no relation whatsoever, just for the sake of training
print(MC[5][1] + MC[-3][1], 'chapters in total')
print(MC[3] + MC[2])

#Slicing
Shōnen = MC[2:] + MC[0]
Shōnen

#Replace
MC[1] = "Seven Deadly Sins", 346
print(MC)

