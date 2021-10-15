#!/usr/bin/env python
# coding: utf-8

# Machine Learning :- is a form of AI that teaches computers to think in a similar way to how humans do.
# Learning and improving upon past experiences.
# It works by exploring data and identifying patterns, and involves minimal human intervention.

# Three Types of Machine Learning :- 
#     1)Supervised Learning(Learn from user data)
#     2)Unsupervised Learning(Learn from mistake)
#     3)Reinforcement Learning(Learn from rewards)

# Numerical Data :- 
#     1)Discrete(Limited to integers)
#     2)Continous(The number that will be the infinite values)

# Categorical Data :- No relation between the two col. of data
# Ordinal Data:- We can judge the first col. data according to second col. data 

# Topic covered:- 
#     mean(average value)
#     median(the mid point value in data)
#     mode(the most common value from the data)

# Scipy Module is used to calculate mode(stats function)
# Sklearn.linear_model Module is used for predicting the values according from given data 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression


# In[3]:


#Mean of the values
x=np.array([10,20,30,40,50,60])
mean=np.mean(x)
print("Mean:-",mean)


# In[5]:


#Median of the values
x=np.array([10,20,30,40,50,60,70])
median=np.median(x)
print("Median:-",median)


# In[7]:


#Mode of the values
x=np.array([10,20,30,40,50,60,10,10])
mode=stats.mode(x)
print("Mode:-",mode)


# In[8]:


print(mode[0],"    ",mode[1])


# Standard Deviation(σ):- is a measure of how dispersed the data is in relation to the mean

# In[9]:


#Standard Deviation
x=np.array([10,11,12,13,14,15])
SD=np.std(x)
print("Standard Deviation:-",SD)


# Variance :- is mean squared difference between each data point and the center of the distribution measured by the mean.

# In[11]:


#Variance of the data
x=np.array([10,20,30,40,50,60])
VAR=np.var(x)
print("Variance:-",VAR)


# In statistics, a Percentile(or a centile) is a score below which a given percentage of scores in its frequency distribution falls.
# 
# numpy.percentile() function used to compute the nth percentile of the given data(array elements) along the specified axis.

# In[18]:


#Percentile of the number
#10 % of data is greater than 15.0
x=np.array([10,20,30,40,50,60])
per=np.percentile(x,10)
print(per)
per=np.percentile(x,30)
print(per)
per=np.percentile(x,60)
print(per)
per=np.percentile(x,60,axis=0,out=None,keepdims=True)
print(per)


# In[24]:


#graph of the data
x=np.array([10,20,30,40,50,60])
y=np.array([1,2,3,4,5,6])
plt.scatter(x,y,color="green")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(color="black",linewidth=0.5)
plt.show()

