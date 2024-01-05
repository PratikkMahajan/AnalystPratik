#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as py


# # Import Data

# In[2]:


df = pd.read_csv(r"C:\Users\mprat\Downloads\Software_Professional_Salaries.csv")


# In[3]:


df


# In[20]:


df.head()


# In[21]:


df.head(10)


# In[22]:


df.tail()


# In[23]:


df.tail(10)


# In[24]:


df.shape


# In[25]:


df.info()


# In[26]:


df.columns


# In[27]:


df.dtypes


# In[28]:


df.isnull().sum()


# In[29]:


df.describe()


# In[30]:


df.duplicated().sum()


# In[4]:


x=df['Location']
print(x)


# In[5]:


y = df['Salary']
print(y)


# In[33]:


df['Job Title'].unique()


# In[34]:


df.select_dtypes(include='object').nunique()


# In[35]:


sns.set(rc={'figure.figsize':(10,7)})
sns.set_style('whitegrid')
sns.countplot(x='Location' ,data=df,palette='RdBu')


# In[6]:


fig = py.histogram(df, x='Location', y='Salary', color='Location',
                   title='Salary(Location Wise) Histogram')

fig.show()


# In[40]:


sns.pairplot(df)


# In[41]:


plt.figure(figsize=(10, 7))
sns.set_style('whitegrid')
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="viridis")
plt.show()


# In[ ]:




