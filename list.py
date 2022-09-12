#!/usr/bin/env python
# coding: utf-8

# # LIST

# In[3]:


list1=[1,2,3,4,5,6,'uday']
print(list1)


# In[4]:


type(list1)


# In[6]:


len(list1)


# In[5]:


list1[2]


# In[7]:


list1[:3]


# In[8]:


list1[-3:]


# In[13]:


list1[0:7:2]


# In[14]:


list1[::2]


# In[15]:


#list can be mutable
list1[0]=100


# In[16]:


list1


# In[17]:


list1.append('Ghorapade')
print(list1)


# In[20]:


list1.insert(6,7)
list1


# In[22]:


list1


# In[24]:


list1copy=list1
list1copy


# In[26]:


list1=['uday']
list2=['ghorapade']
list1.extend(list2)
list1


# In[27]:


list3=list1 + list2
list3


# In[30]:


list3.insert(3,4)
list3


# In[32]:


rem=list3.pop(3)
print(rem)


# In[ ]:




