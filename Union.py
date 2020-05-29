#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np

#define a func whos output is immutable (a set)
def sets(list1, list2, deleteList):

#inputs
    #list1
    #list2
    #deleteList 
#outputs
    #resultList

    #union of List1 + List2
    interList = sorted(np.unique(list1+list2), key = len, reverse = True) #sort by descending length

    #remove the intersection of interList and deleteList
    resultList = set(interList) - set(deleteList)
    resultList = sorted(resultList, reverse = True)  #sort by reverse alphabetical
    
    resultList = set(resultList) #convert result to a set (sets are immutable in python)
    
    return(resultList)

def main():
    
    print(sets(['one', 'two', 'three'], ['one', 'two', 'five', 'six'], ['two', 'five']))

main()


# In[45]:





# In[ ]:




