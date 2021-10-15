#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import PIL
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


print(dir(PIL.__name__))


# In[6]:


img=Image.open("main.png")


# In[7]:


display(img)


# In[8]:


img_array=np.array(img)


# In[9]:


print(img_array)


# In[10]:


print("Dimension:- ",img_array.ndim)
print("Shape:- ",img_array.shape)
print("Data Type:-",img_array.dtype)


# In[11]:


new_array=np.full(img_array.shape,254)


# In[12]:


mod_array=new_array-img_array


# In[13]:


print("Dimension:- ",mod_array.ndim)
print("Shape:- ",mod_array.shape)
print("Data Type:-",mod_array.dtype)


# In[14]:


#chaning the data type of new array
mod_array=mod_array.astype(np.uint8)


# In[15]:


a=Image.fromarray(mod_array)


# In[16]:


display(a)


# In[17]:



a.rotate(45).show()


# In[ ]:




