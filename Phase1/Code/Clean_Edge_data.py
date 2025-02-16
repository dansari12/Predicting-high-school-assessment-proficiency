#!/usr/bin/env python
# coding: utf-8

# ## Phase 1: Part 3: Clean up of EDGE data files. This notebook contains code that cleans and preps the edge data file that contains the school neighborhood income ratio estimate data
# #### Notes: The estimates reflect the income-to- poverty ratio (IPR), which is the percentage of family income that is above or below the federal poverty threshold set for the family’s size and structure. The IPR indicator ranges from 0 to 999.1 Lower IPR values indicate a greater degree of poverty. A family with income at the poverty threshold has an IPR value of 100. The Census Bureau calculates the IPR based on money income reported for families. 

# ### Loading necessary libraries

# In[3]:


import pandas
pandas.__version__
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


cd /Users/dansa/Documents/GitHub/Phase1/Data/EDGE


# #### Loading in file and reading the first 5 rows

# In[5]:


edge = pandas.read_csv("sch_neighborhood_poverty.csv")
edge.head()


# Reviewing the datatypes and shape of the file

# In[6]:


edge.dtypes


# In[7]:


edge.shape


# #### Adding leading zeros to Federal school ID and checking to see if change was applied accurately

# In[8]:


edge['NCESSCH'] = edge['NCESSCH'].apply(lambda x: '{0:0>12}'.format(x))


# In[9]:


edge['NCESSCH_length'] = edge['NCESSCH'].map(str).apply(len)


# In[10]:


edge.head()


# In[11]:


edge.describe()


# #### Checking to make sure School ID is unique and free of duplicates

# In[12]:


edge['NCESSCH'].is_unique


# In[13]:


edge.drop(edge.columns[[4]], axis =1, inplace=True)


# In[14]:


edge.rename(columns={'IPR_EST':'Income_Poverty_ratio'}, inplace=True)


# In[15]:


edge.head()


# #### Use heatmap to determine if there are missing data

# In[16]:


sns.heatmap(edge.isnull(),yticklabels=False,cbar=True,cmap='viridis')


# #### Checking the distribution

# In[17]:


edge.hist()


# In[18]:


from pandas.plotting import scatter_matrix
scatter_matrix(edge, alpha=0.2, figsize=(6, 6), diagonal='kde')


# In[19]:


#### Saving final copy of the merge file for later use


# In[20]:


edge.to_csv (r'/Users/dansa/Documents/GitHub/Phase1/Data/EDGE/Clean_EDGE.csv', index = False, header=True)

