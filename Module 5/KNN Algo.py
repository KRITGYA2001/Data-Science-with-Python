#!/usr/bin/env python
# coding: utf-8

# In[1]:


#It find out the distance for all the points from a specific point
#Taking sample data


# In[2]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# In[3]:


#creating the flower data sample file
file=pd.read_csv("Flowertestingdata.csv")


# In[4]:


print(file.head())
print(file.head())


# In[13]:


x=file.loc[:,"sepal_length":"petal_width"]
y=file.loc[:,"class"]


# In[14]:


Knn=KNeighborsClassifier()
Knn.fit(x,y)


# In[15]:


test_data=[[5.1,3.2,1.2,1.2]]
predict=Knn.predict(test_data)
print(predict)


# In[9]:


from matplotlib import pyplot as plt


# In[11]:


plt.xlabel("feature")
plt.ylabel("class")

c=file.loc[:,"sepal_length"]
b=file.loc[:,'class']
plt.scatter(c,b,color='blue',label="sepal_length")


c=file.loc[:,"sepal_width"]
b=file.loc[:,'class']
plt.scatter(c,b,color='green',label="sepal_width")


c=file.loc[:,"petal_length"]
b=file.loc[:,'class']
plt.scatter(c,b,color='yellow',label="peta_length")

c=file.loc[:,"petal_width"]
b=file.loc[:,'class']
plt.scatter(c,b,color='cyan',label="peta_width")

#plt.plot(test,predict,color="orange",label="test_data")
#we will use this command in seaborn

plt.legend()
plt.show()

