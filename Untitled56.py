#!/usr/bin/env python
# coding: utf-8

# Create a function that takes three parameters where:
# x is the start of the range (inclusive).
# y is the end of the range (inclusive).
# n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.

# In[4]:


def list_operation(x, y, n):
    result = []
    for i in range(x, y+1):
        if i % n == 0:
            result.append(i)
    return result


# In[5]:


list_operation(1, 10, 3)


# In[6]:


list_operation(7, 9, 2)


# In[7]:


list_operation(15, 20, 7)


# Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.
# 

# In[36]:


def simon_says(lst1, lst2):
    return lst2[1:] == lst1[:-1]


# In[37]:


simon_says([1, 2], [5, 1])


# In[38]:


simon_says([1, 2], [5, 5])


# In[39]:


simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])


# In[40]:


simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])


# A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.
# Create a function that takes in a list of names and returns the name of the secret society.
# 

# In[42]:


def society_name(names):
    first_letters = [name[0].upper() for name in names]
    sorted_letters = sorted(first_letters)
    return ''.join(sorted_letters)


# In[43]:


society_name(["Adam", "Sarah", "Malcolm"])


# In[44]:


society_name(["Harry", "Newt", "Luna", "Cho"])


# In[45]:


society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])


# An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
# 

# In[49]:


def is_isogram(word):
    word = word.lower()
    letters = set(word)
    return len(letters) == len(word)


# In[50]:


is_isogram("Algorism")


# In[51]:


is_isogram("PasSword")


# In[52]:


is_isogram("Consecutive") 


# Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
# 

# In[53]:


def is_in_order(word):
    if word ==''.join(sorted(word)):
        return True
    elif word == ''.join(sorted(word, reverse=True)):
        return True
    else:
        return False


# In[54]:


is_in_order("abc")


# In[55]:


is_in_order("edabit")


# In[57]:


is_in_order("123")


# In[59]:


is_in_order("xyzz")


# In[ ]:




