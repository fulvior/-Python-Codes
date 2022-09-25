#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math
import numpy as np

dim = int(input("Inserisci la dimensione del vettore: "))
print("Inserisci gli elementi del vettore separati da uno spazio: ")

elements = list(map(float, input().split()))

    
vector = np.array(elements).reshape(dim)
print(vector)

v = 0
for i in range(len(vector)):
    v = v + vector[i]**2
    
v = math.sqrt(v)
print("la norma del vettore inserito è: ", v)

    


# In[ ]:




