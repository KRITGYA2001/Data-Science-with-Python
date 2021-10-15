#!/usr/bin/env python
# coding: utf-8

# # Multiple Regression

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[3]:


'''Depending upon 2-3 col. to predict the value of the next col.'''
file=pd.read_csv('MRtesting1.csv')


# In[4]:


print(file.head())
print(file.tail())


# In[5]:


x=file[['Table1','Table2']]
y=file['Table3']


# In[6]:


lst=LinearRegression()
lst.fit(x,y)


# In[7]:


predict=lst.predict([[1,10],[3,30]])
print(predict)


# In[ ]:




