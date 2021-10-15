#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import random as rd


# In[36]:


file=pd.read_csv("cars.csv")


# In[25]:


file.dropna(inplace=True)


# In[29]:


file['distance'].fillna(12,inplace=True)
file['consume'].fillna(11,inplace=True)


# In[37]:


#Cleaning distance
for i in file.index:
    a=file.loc[i,"distance"]
    try:
        if int(a)>0:
            file.loc[i,"distance"]=rd.randint(1,100)
    except:
        file.loc[i,"distance"]=rd.randint(1,100)


# In[38]:


#Cleaning consume
for i in file.index:
    a=file.loc[i,"consume"]
    try:
        if int(a)>0:
            pass
    except:
        file.loc[i,"consume"]=rd.randint(1,100)


# In[39]:


#Data File
file.to_csv("carsample.csv",index=False)


# In[2]:


print("\U0001f600")


# In[ ]:


# checking the distribution of categorical data
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())


# In[ ]:


# encoding "Fuel_Type" Column
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

# encoding "Seller_Type" Column
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# encoding "Transmission" Column
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)


# In[ ]:




