#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#It is used for classification
#Create a model to predict any value by Learning from data sets
'''
class of positive=6
class of negative=5

formula for information gain
information gain=I(p,n)=-p/p+n=log>2(p/p+n)-(n/(p+n)) log>2(n/p+n)

Entropy E(A)=sum Pi+Ni/p+n * information gain

Overall Gain(A)=information gain - Entropy
'''
# In[3]:


from sklearn.tree import DecisionTreeClassifier


# In[4]:


file=pd.read_csv("DTcars.csv")


# In[5]:


print(file.head())
print(file.tail())


# In[6]:


x=file.loc[:,"main":"milage"]
y=file.loc[:'choice']


# In[7]:


# Max leaf node = (greatest number)
Tree=DecisionTreeClassifier(max_leaf_nodes=3,random_state=0)
Tree.fit(x,y)
#Maximun point of view (depending upon parameters) on our dataset(leaf nodes)


# In[8]:


predict=Tree.predict([[1,2,1,1,2]])
print(predict)


# In[ ]:




