#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import data1
import pandas as pd
csv_file = "/Users/louis/Desktop/Ironhack/Git/lab-customer-analysis-round-1/files_for_lab/file1.csv"
data1 = pd.read_csv(csv_file)


# In[6]:


#import data2
import pandas as pd
csv_file = "/Users/louis/Desktop/Ironhack/Git/lab-customer-analysis-round-1/files_for_lab/file2.csv"
data2 = pd.read_csv(csv_file)


# In[7]:


#import data3
import pandas as pd
csv_file = "/Users/louis/Desktop/Ironhack/Git/lab-customer-analysis-round-1/files_for_lab/file3.csv"
data3 = pd.read_csv(csv_file)


# In[26]:


#concenate 

pd.concat([data1, data2, data3]) 


# In[8]:


data1.head()


# In[11]:


#drop education
data1.drop(columns = ["Education"], inplace = True)


# In[10]:


#drop open compaints
data1.drop(columns = ["Number of Open Complaints"], inplace = True)


# In[12]:


data1.head()


# In[16]:


data1[Customer Lifetime Value].astype(numerical)


# In[19]:


#check duplicate

data1.drop_duplicates()


# In[27]:


#0 or less income 

data1[data1['Income'] <= 0]


# In[ ]:




