#!/usr/bin/env python
# coding: utf-8

# # Critical Roll

# In[11]:


import random
from tkinter import *  ##GUI Tool
import pandas as pd

#Create Dinner List

dinner = {'DinnerID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
         'Restaurant': ['Peace, Love, Pizza', 'Vespucci’s Italian Restaurant', 'Zama Mexican Cuisine', 
                        'Marco’s Pizza', 'Firehouse Subs', 'Saigon Cafe', 'Hong Kong City', 'Ichiban Grill', 'Buffalo’s Cafe', 
                        'Steak & Shake', 'O’Charley’s', 'Five Guys', 'Los Bravos Mexican', 'Sidelines Grill', 
                        'Johnny’s NY Style Pizza', 'Keegan’s Public House', 'iHOP', 'Waffle House', 'Moon’s Wings & Hibachi', 
                        'Chilli’s']}
df = pd.DataFrame (dinner, columns = ['DinnerID','Restaurant'])
print(df)


# In[ ]:


#Pick the Restaurant...


# In[14]:


print("Restaurants for tonight are either...")
df.sample(2)


# In[ ]:




