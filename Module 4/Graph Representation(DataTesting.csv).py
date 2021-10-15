#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


# In[2]:


file=pd.read_csv('Datatesting.csv')


# In[17]:


print(file.head())
print(file.tail())


# In[18]:


print(file.describe())


# In[22]:


print(file.columns)


# In[23]:


sb.pairplot(file)


# In[3]:


#Get all the unique hobbies
Uhobbies=[]
for i in file.index:
    a=file.loc[i,"Hobbies"]
    if a in Uhobbies:
        pass
    else:
        Uhobbies.append(a)     


# In[4]:


print("All unique hobbies")
a=pd.DataFrame(data=Uhobbies)
print(a)


# In[13]:


#Most favourate number from data
MfavNum=[]
for i in file.index:
    a=file.loc[i,"Fav Number"]
    MfavNum.append(int(a)) 
    
#Creating new list contains only one fav number (no repeating)
Num=[]
for i in MfavNum:
    if i in Num:
        pass
    else:
        Num.append(int(i))
              

#Calculating the most appeared element        
res=0
lst=[]
for i in Num:
    counts=MfavNum.count(i)
    lst.append(int(counts))            


# In[71]:


print("Fav Number and Repetition of the Fav Number")
print(pd.DataFrame(lst,Num))


# In[69]:


plt.bar(Num,lst,width=10)
plt.xlabel("Fav Number")
plt.ylabel("Repetition")
xmin,xmax=plt.xlim()
sf=0.1
plt.xlim(xmin*sf,xmax*sf)
plt.show()


# In[17]:


#Separate the data with age <15 and coding as hobby
data=[]
for i in file.index:
    age=file.loc[i,"Age"]
    hobbies=file.loc[i,"Hobbies"]
    if int(age)<15 and hobbies.capitalize()=='Coding':
        c=[file.loc[i,"Name"],age,hobbies,file.loc[i,"Fav Color"],file.loc[i,"Fav Number"]]
        data.append(c)


# In[62]:


print("Table with data of age<15 and coding as hobby")
print(pd.DataFrame(data=data))
print("\n")


# In[59]:


#Calculate average age of the dataset
Age_data=[]
for i in file.index:
    a=file.loc[i,"Age"]
    Age_data.append(int(a))   
    
avg=0
for i in Age_data:
    avg=avg+i
avg=avg//len(Age_data)    


# In[78]:


plt.plot(Age_data,marker="o",ms=3,mfc="cyan")
plt.title("Person with Age")
plt.xlabel("Person Number")
plt.ylabel("Age")
plt.grid(color="black",linestyle="--")
plt.show()


# In[57]:


#How many people have hobby as travelling
hobbies_data=[]
for i in file.index:
    hobbies=file.loc[i,"Hobbies"]
    if hobbies.lower()=='travelling':
        c=[file.loc[i,"Name"],file.loc[i,"Age"],file.loc[i,"Hobbies"],file.loc[i,"Fav Number"],file.loc[i,"Fav Color"]]
        hobbies_data.append(c)


# In[58]:


print("Table with People have hobby as travelling")
print(pd.DataFrame(data=hobbies_data))
print("\n\n")


# In[ ]:




