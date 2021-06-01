#!/usr/bin/env python
# coding: utf-8
import http
import json
import os

import httplib2
import pandas as pd
import sklearn


def usage_to_df():
    http = httplib2.Http()
    status, response = http.request(f'https://play.pokemonshowdown.com/data/sets/gen8ou.json')
    set = json.loads(response)
    set = set['dex']
    status, response = http.request(f'https://play.pokemonshowdown.com/data/pokedex.json')
    dex = json.loads(response)

    path = f"https://www.smogon.com/stats/2021-03/gen8ou-1825.txt"
    df = pd.read_csv(path, engine='python', encoding='cp1252', error_bad_lines=False,
                     skiprows=[0, 1, 2, 4], sep="|")
    df = df[:-1]
    df = df.drop(' .1', axis=1)
    df = df.rename(columns={' %       .1': '%'})
    name = "gen8OU"
    filename = f"{name}"
    file_path = f'output/{filename}.csv'
    if not os.path.exists(file_path):
        df.to_csv(f'output/{filename}.csv', mode='a',
                  header=['null', 'Rank', "Pokemon", "Usage%", "Raw", "Raw%", 'Real', "Real%"], index=False)
    usage = pd.read_csv(f"output/{filename}.csv")

    del usage['null']
    indexNames = usage[usage['Rank'] > 57].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 40.0].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 48.0].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 15.0].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 12.0].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 21.0].index
    usage.drop(indexNames, inplace=True)
    indexNames = usage[usage['Rank'] == 56.0].index
    usage.drop(indexNames, inplace=True)

    list_poke_set = usage['Pokemon'].tolist()
    i = 0
    while i < len(list_poke_set):
        list_poke_set[i] = list_poke_set[i].strip()
        i = i + 1

    list_poke_dex = usage['Pokemon'].tolist()
    i = 0
    while i < len(list_poke_dex):
        list_poke_dex[i] = list_poke_dex[i].strip()
        list_poke_dex[i] = list_poke_dex[i].replace(" ", '')
        list_poke_dex[i] = list_poke_dex[i].replace("-", '')
        list_poke_dex[i] = list_poke_dex[i].lower()
        i = i + 1

    df = pd.DataFrame(
        columns=['Name', 'num', 'hp', 'atk', 'def', 'spa', 'spd', 'spe'])

    i = 0
    while i < len(list_poke_dex):
        pokemon_set = set[list_poke_set[i]]
        for j in pokemon_set:
            set_name = j
        list = [dex[list_poke_dex[i]]['name'], dex[list_poke_dex[i]]['num'],
                (dex[list_poke_dex[i]]['baseStats']['hp'] + (pokemon_set[set_name]['evs'].get('hp', 0) / 4)) * 2 + 110,
                (dex[list_poke_dex[i]]['baseStats']['atk'] + (pokemon_set[set_name]['evs'].get('atk', 0) / 4)) * 2 + 5,
                (dex[list_poke_dex[i]]['baseStats']['def'] + (pokemon_set[set_name]['evs'].get('def', 0) / 4)) * 2 + 5,
                (dex[list_poke_dex[i]]['baseStats']['spa'] + (pokemon_set[set_name]['evs'].get('spa', 0) / 4)) * 2 + 5,
                (dex[list_poke_dex[i]]['baseStats']['spd'] + (pokemon_set[set_name]['evs'].get('spd', 0) / 4)) * 2 + 5,
                (dex[list_poke_dex[i]]['baseStats']['spe'] + (pokemon_set[set_name]['evs'].get('spe', 0) / 4)) * 2 + 5,
                ]
        df.loc[i] = list
        i = i + 1
    return df

def clustering_set():
    df = usage_to_df()
    feature_cols = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
    return sklearn.utils.Bunch(data= (df[feature_cols].to_numpy()).astype('float') )
