
# coding: utf-8

# In[1]:


import numpy as np
def L1(l1hat, l1):
    return np.sum(np.absolute(l1hat - l1))

