#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.__version__


# In[2]:


import pandas as pd
import numpy as np
dict1 = {"name":["Rahul","Rohan","Atul","Karan"],
       "Marks": [52,68,25,55],
      "city": ["agra","Mathura","Delhi","Noida"]
      }
df = pd.DataFrame(dict1)
print(df)


# In[3]:


df.to_csv('friends.csv')


# In[4]:


df.to_csv('friends_index_false.csv', index= False)


# In[5]:


df.head(2)


# In[6]:


df.tail(2)


# In[7]:


df.describe()


# In[8]:


rahul= pd.read_csv('rahul.csv.csv')


# In[9]:


rahul


# In[10]:


rahul['Speed'][0]= 48


# In[11]:


rahul


# In[12]:


ser = pd.Series(np.random.rand(34))


# In[13]:


type(ser)


# In[14]:


newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))


# In[15]:


type(newdf)
newdf.head()


# In[16]:


newdf.describe()


# In[17]:


newdf.dtypes


# In[18]:


newdf.dtypes


# In[19]:


newdf.describe()


# In[20]:


newdf.describe()


# In[21]:


newdf.dtypes


# In[22]:


newdf[0][0]= "rahul"


# In[23]:


newdf.dtypes


# In[24]:


newdf.head()


# In[25]:


newdf.index


# In[26]:


newdf.columns


# In[27]:


newdf.to_numpy()


# In[28]:


newdf[0][0]= 0.3


# In[29]:


newdf.head()


# In[30]:


newdf.T


# In[31]:


newdf.T


# In[32]:


newdf.head()


# In[33]:


newdf.sort_index(axis=1,ascending=False)


# In[34]:


type(newdf[0])


# In[35]:


newdf.head()


# In[36]:


newdf2 = newdf.copy()


# In[37]:


newdf2[0][0]= 95887


# In[38]:


newdf


# In[39]:


newdf.loc[0,0]= 785


# In[40]:


newdf.head(2)
   


# In[41]:


newdf.columns = list("ABCDE")


# In[42]:


newdf.head()


# In[43]:


newdf.loc[0,'A']= 6545


# In[44]:


newdf.head()


# In[45]:


newdf.loc[[1,2],['C','D']]


# In[46]:


newdf.head()


# In[47]:


newdf.loc[:,['C','D']]


# In[48]:


newdf.loc[[1,2],:]


# In[49]:


newdf.loc[(newdf['A']<0.3)&(newdf['C']>0.1)]


# In[50]:


newdf.head(2)


# In[51]:


newdf.iloc[0,4]


# In[52]:


newdf.iloc[[0,5],[1,3]]


# In[53]:


newdf.head(3)


# In[54]:


newdf.drop([1,5], axis=0 , inplace=True)


# In[55]:


newdf.head(3)


# In[56]:


newdf.reset_index(drop=True, inplace=True)


# In[63]:


newdf.head(3)


# In[68]:


newdf.drop(['A','B'],axis=1,inplace=True)


# In[69]:


newdf


# In[70]:


newdf.head(3)


# In[77]:


newdf.loc[:,['C']]= 89


# In[81]:


newdf.head()


# In[82]:


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'np.', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})


# In[83]:


df


# In[85]:


df.dropna(how='all')


# In[ ]:


df

