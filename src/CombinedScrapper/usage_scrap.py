#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import httplib2
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer
import os

http = httplib2.Http()
status, response = http.request('https://www.smogon.com/stats/')
sublink = []
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        sublink.append(link['href'])
sublink = sublink[1:]

http = httplib2.Http()
for i in sublink:
    status, response = http.request(f'https://www.smogon.com/stats/{i}')
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].startswith("gen"):
                if link['href'].endswith(".txt"):
                    path = f"https://www.smogon.com/stats/{i}{link['href']}"
                    df = pd.read_csv(path, engine='python', encoding='cp1252', error_bad_lines=False,
                                     skiprows=[0, 1, 2, 4], sep="|")
                    df = df[:-1]
                    df = df.drop(' .1', axis=1)
                    df = df.rename(columns={' %       .1': '%'})
                    name = link['href'].split('-')[0]
                    filename = f"{i[:-1]}-{name}"
                    file_path = f'output/{filename}.csv'
                    if os.path.exists(file_path):
                        df.to_csv(f'output/{filename}.csv', mode='a', header=False, index=False)
                    else:
                        df.to_csv(f'output/{filename}.csv', header=False, index=False)


# same but new version (not tested cause i don t have computer)
def custom(year_wanted, class_wanted):
    import httplib2
    import pandas as pd
    from bs4 import BeautifulSoup, SoupStrainer
    import os

    http = httplib2.Http()
    status, response = http.request('https://www.smogon.com/stats/')
    sublink = []
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            sublink.append(link['href'])
    sublink = sublink[1:]

    http = httplib2.Http()
    i = year_wanted
    status, response = http.request(f'https://www.smogon.com/stats/{i}')
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].startswith("gen"):
                if link['href'].endswith(".txt") and class_wanted in link['href']:

                    path = f"https://www.smogon.com/stats/{i}{link['href']}"
                    df = pd.read_csv(path, engine='python', encoding='cp1252', error_bad_lines=False,
                                     skiprows=[0, 1, 2, 4], sep="|")
                    df = df[:-1]
                    df = df.drop(' .1', axis=1)
                    df = df.rename(columns={' %       .1': '%'})
                    name = link['href'].split('-')[0]
                    filename = f"{i[:-1]}-{name}"
                    file_path = f'output/{filename}.csv'
                    if os.path.exists(file_path):
                        df.to_csv(f'output/{filename}.csv', mode='a', header=False, index=False)
                    else:
                        df.to_csv(f'output/{filename}.csv', header=False, index=False)
    return pd.read_csv("output/{filename}.csv")
