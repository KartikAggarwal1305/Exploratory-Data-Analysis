#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


data = pd.read_csv(r"D:\Great Learning\EDA\IPL Matches 2008-2020.csv")


# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.info


# In[11]:


data.describe()


# In[9]:


data.columns


# In[10]:


data.isna().any()


# In[15]:


data['date'].unique()


# In[27]:


data.iloc[data['result_margin'].idxmax()]


# In[37]:


win_by_wickets = data[data['result']== 'wickets']
print(win_by_wickets)


# In[52]:


fig_dims = (30, 8)
fig, ax = plt.subplots(figsize = fig_dims)
sns.countplot(x='winner' , data = data)
plt.show()


# In[54]:


data1 = data.winner.value_counts()
sns.barplot(y = data1.index, x = data1  )


# In[66]:


probability_of_win = data['toss_winner'] == data['winner']
probability_of_win.groupby(probability_of_win).size()


# In[68]:


get_ipython().set_next_input("sns.countplot('Which amongst the following is Artificial Juridical Person");get_ipython().run_line_magic('pinfo', 'Person')
*probabilty_of_win)


# In[ ]:




