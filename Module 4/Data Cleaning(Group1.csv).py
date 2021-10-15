#!/usr/bin/env python
# coding: utf-8

# # Working on cleaning the data

# In[1]:


import pandas as pd
import random as rd


# In[2]:


file=pd.read_csv('group1.csv')


# In[3]:


file.dropna(inplace=True)
file['Age'].dropna(inplace=True)
file['Fav Number'].dropna(inplace=True)


# In[4]:


file['Name'].fillna('random',inplace=True)
file['Hobbies'].fillna('coding',inplace=True)
file['Fav Color'].fillna('blackandwhite',inplace=True)


# In[5]:


#Cleaning age
for i in file.index:
    a=file.loc[i,"Age"]
    try:
        if int(a)>110:
            file.loc[i,"Age"]=65
    except:
        file.loc[i,"Age"]=45TT


# In[6]:


#Fav Number Cleaning
for i in file.index:
    a=file.loc[i,"Fav Number"]
    try:
        if int(a)>0:
            pass
    except:
        file.loc[i,"Fav Number"]=rd.randint(1,100)


# In[7]:


#Removing the integer name input
for i in file.index:
    a=file.loc[i,"Name"]
    try:
        if int(a)>0:
            file.loc[i,"Name"]="Random"
    except:
        pass


# In[8]:


#Removing the integer color input
for i in file.index:
    a=file.loc[i,"Fav Color"]
    try:
        if int(a)>0:
            file.loc[i,"Fav Color"]="BlackandWhite"
    except:
        pass


# In[9]:


#Data File
file.to_csv("Datatesting.csv",index=False)


# In[10]:


#Get all the unique hobbies
Uhobbies=[]
for i in file.index:
    a=file.loc[i,"Hobbies"]
    if a in Uhobbies:
        pass
    else:
        Uhobbies.append(a)     


# In[30]:


print("All unique Hobbies are:- ",Uhobbies)  


# In[12]:


#Most favourate number from data
MfavNum=[]
for i in file.index:
    a=file.loc[i,"Fav Number"]
    MfavNum.append(int(a))     


# In[13]:


#Creating new list contains only one fav number (no repeating)
Num=[]
for i in MfavNum:
    if i in Num:
        pass
    else:
        Num.append(i)

#Calculating the most appeared element        
res=0
for i in Num:
    counts=MfavNum.count(i)
    if res<counts:
        res=counts
        ele=i        


# In[14]:


print("The Most Favourate Number is :- ",ele)


# In[28]:


#Separate the data with age <15 and coding as hobby
data=[]
for i in file.index:
    age=file.loc[i,"Age"]
    hobbies=file.loc[i,"Hobbies"]
    if int(age)<15 and hobbies.capitalize()=='Coding':
        c=[file.loc[i,"Name"],age,hobbies,file.loc[i,"Fav Color"],file.loc[i,"Fav Number"]]
        data.append(c)


# In[29]:


print("Person with age less than 15 and coding as hobbies are:- ")
for i in data:
    print(i)


# In[22]:


#Calculate average age of the dataset
Age_data=[]
for i in file.index:
    a=file.loc[i,"Age"]
    Age_data.append(int(a))   
    
avg=0
for i in Age_data:
    avg=avg+i
avg=avg//len(Age_data)    


# In[23]:


print("The average height of the age data is:- ",avg)


# In[26]:


#How many people have hobby as travelling
hobbies_data=[]
for i in file.index:
    hobbies=file.loc[i,"Hobbies"]
    if hobbies.lower()=='travelling':
        c=[file.loc[i,"Name"],file.loc[i,"Age"],file.loc[i,"Hobbies"],file.loc[i,"Fav Number"],file.loc[i,"Fav Color"]]
        hobbies_data.append(c)


# In[27]:


print("The People's who hobbies are travelling are:- ")
for i in hobbies_data:
    print(i)

