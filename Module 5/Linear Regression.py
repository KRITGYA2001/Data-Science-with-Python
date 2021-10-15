#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# # Linear Regression
'''
#Sample Data
Table1     Table2
  65         99
  44         55
  66         96
  88         88
  44         55 
  55         44
  22         22
  10         01
'''  
# In[4]:


#Operation on csv file
file=pd.read_csv("LRtesting1.csv")


# In[5]:


#head function (prints first 5 data)
#tail function (prints last 5 data)
print(file.head())
print(file.tail())


# In[6]:


x=file["Table1"].values[:,np.newaxis]
y=file["Table2"].values


# In[7]:


#creating the LR machine (trail 1)
lst=LinearRegression()
#fit x and y 
lst.fit(x,y)


# In[8]:


test_data=[[10],[11],[12],[13],[14]]
predict=lst.predict(test_data)
print(predict)


# In[9]:


#creating the LR machine (trail 2)
file=pd.read_csv("LRtesting2.csv")


# In[10]:


#head function (prints first 5 data)
#tail function (prints last 5 data)
print(file.head())
print(file.tail())


# In[11]:


x=file["Table1"].values[:,np.newaxis]
y=file["Table2"].values


# In[12]:


lst=LinearRegression()
lst.fit(x,y)


# In[13]:


test_data=[[11],[12],[13],[14],[15]]
predict=lst.predict(test_data)
print(predict)


# In[14]:


'''from matplotlib import pyplot as plt'''
#Best fit Line
#STEP 1 :- cal. the mean value of x and y


# In[15]:


x=[1,2,3,4,5,6,7,8,9,10]
print(np.mean(x))


# In[16]:


'''
Calculate slope m
m= sum(x-X)(y-Y)/(x-X)^2
c=Y-mX
'''


# In[17]:


file=pd.read_csv("LRtesting2.csv")


# In[18]:


x=file["Table1"].values[:,np.newaxis]
y=file["Table2"].values


# In[19]:


plt.scatter(x,y)
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




