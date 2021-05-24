#!/usr/bin/env python
# coding: utf-8

# In[1]:


import httplib2
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('https://www.smogon.com/stats/')
sublink = []
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        sublink.append(link['href'])
sublink = sublink[1:]


# In[6]:


http = httplib2.Http()
for i in sublink:
    status, response = http.request(f'https://www.smogon.com/stats/{i}')
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].startswith("gen"):
                if link['href'].endswith(".txt"):
                    path = f"https://www.smogon.com/stats/{i}{link['href']}"
                    df = pd.read_csv(path,engine='python',encoding='cp1252', error_bad_lines=False, skiprows=[0, 1,2,4], sep= "|")
                    df = df[:-1]
                    df = df.drop(' .1', axis=1)
                    df = df.rename(columns={' %       .1': '%'})
                    filename = f"{i[:-1]}-{link['href']}"
                    df.to_csv(f'output/{filename}.csv')


# In[ ]:




