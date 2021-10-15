#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import seaborn as sb


# In[21]:


file=pd.read_csv("IRIS.csv")
f=sb.load_dataset('iris')


# In[3]:


print(file.head())
print(file.tail())


# In[4]:


x=file.loc[:,"sepal_length":"petal_width"]
y=file.loc[:,"species"]


# In[5]:


Knn=KNeighborsClassifier()
Knn.fit(x,y)


# In[7]:


test_data=[[5.0,3.6,1.4,0.2],[6.7,3.0,5.2,2.3],[1,2,3,4],[2,3,2,4]]
predict=Knn.predict(test_data)
print(predict)


# # Graph Representation

# In[9]:


plt.xlabel("Specifications")
plt.ylabel("IRIS species")
plt.title("IRIS Dataset")


sepal_length=file.loc[:,"sepal_length"]
b=file.loc[:,"species"]
plt.scatter(sepal_length,b,color="blue",label="sepal_length")


sepal_width=file.loc[:,"sepal_width"]
b=file.loc[:,"species"]
plt.scatter(sepal_width,b,color="cyan",label="sepal_width")


petal_length=file.loc[:,"petal_length"]
b=file.loc[:,"species"]
plt.scatter(petal_length,b,color="red",label="petal_length")


petal_width=file.loc[:,"petal_width"]
b=file.loc[:,"species"]
plt.scatter(petal_width,b,color="green",label="petal_width")

plt.legend()
plt.show()


# In[25]:


#Clear view  of points
plt.subplot(2,1,1)
sb.swarmplot(x='species',y="petal_length",data=f)

plt.subplot(2,1,2)
sb.swarmplot(x='species',y="petal_width",data=f)
plt.show()


# In[26]:


#Clear view  of points
plt.subplot(2,1,1)
sb.swarmplot(x='species',y="sepal_length",data=f)

plt.subplot(2,1,2)
sb.swarmplot(x='species',y="sepal_width",data=f)
plt.show()


# In[19]:


#Sepal__length
plt.subplot(2, 3, 1)
plt.hist(sepal_length,color="cyan")
plt.grid(color="black",linewidth=0.5)
plt.title("Sepal length")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#Sepal__width
plt.subplot(2, 3, 2)
plt.hist(sepal_width,color="cyan")
plt.grid(color="black",linewidth=0.5)
plt.title("Sepal Width")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


#petal__length
plt.subplot(2, 3, 3)
plt.hist(petal_length,color="cyan")
plt.grid(color="black",linewidth=0.5)
plt.title("Petal length")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#petal__width
plt.subplot(2, 3, 4)
plt.hist(petal_width,color="cyan")
plt.grid(color="black",linewidth=0.5)
plt.title("Petal Width")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


# In[32]:


#All Relationship Graph in iris dataset
sb.pairplot(f,hue="species",palette="inferno")
plt.show()


# In[ ]:




