#!/usr/bin/env python
# coding: utf-8

# # Soluções

# In[229]:


Eqs1 = []
Eqs1.append(Eq(4*x-3*y+2*z,60))
Eqs1.append(Eq((x-10)**2+y**2+z**2,72))
Eqs1.append(Eq(2*x-9*y+z,20))
solve(Eqs1, x,y,z)

