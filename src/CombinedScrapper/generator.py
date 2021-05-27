#!/usr/bin/env python
# coding: utf-8

# In[1]:
import json
import httplib2
import pandas as pd
import numpy
import sklearn

def pokedex():
    http = httplib2.Http()
    status, response = http.request(f'https://play.pokemonshowdown.com/data/pokedex.json')
    pokedex = json.loads(response)
    list_pokemon = []
    #for pokemon in pokedex:
         #if pokedex[pokemon]['num'] > 151:
             #list_pokemon.append(pokemon)

    for pokemon in pokedex:
        if pokedex[pokemon]['num'] < 1:
            list_pokemon.append(pokemon)

    for pokemon in list_pokemon:
        del pokedex[pokemon]

    list_pokemon = []
    for pokemon in pokedex:
        if str(pokedex[pokemon].get('tier', "")) == "":
            list_pokemon.append(pokemon)
        if str(pokedex[pokemon].get('tier', "")) == "Illegal":
            list_pokemon.append(pokemon)
        #if str(pokedex[pokemon].get('evos', "")) != "":
            #list_pokemon.append(pokemon)
    list_pokemon = set(list_pokemon)
    for pokemon in list_pokemon:
        del pokedex[pokemon]

    list_pokemon = []
    for pokemon in pokedex:
        if str(pokedex[pokemon].get('genderRatio', "")) != "":
            del pokedex[pokemon]['genderRatio']
        del pokedex[pokemon]['heightm']
        del pokedex[pokemon]['weightkg']
        if str(pokedex[pokemon].get('color', "")) != "":
            del pokedex[pokemon]['color']
        if str(pokedex[pokemon].get('evos', "")) != "":
            del pokedex[pokemon]['evos']
        del pokedex[pokemon]['eggGroups']
        if str(pokedex[pokemon].get('baseSpecies', "")) != "":
            del pokedex[pokemon]['baseSpecies']
        if str(pokedex[pokemon].get('prevo', "")) != "":
            del pokedex[pokemon]['prevo']
        if str(pokedex[pokemon].get('gender', "")) != "":
            del pokedex[pokemon]['gender']
        list_pokemon.append(pokemon)
        if str(pokedex[pokemon]['abilities'].get('1', "")) == "":
            pokedex[pokemon]['abilities']['1'] = 'none'
        if str(pokedex[pokemon]['abilities'].get('H', "")) == "":
            pokedex[pokemon]['abilities']['H'] = 'none'

    return pokedex


def pokedex_df():
    # Create a DataFrame object
    df = pd.DataFrame(
        columns=['Name', 'num', 'hp', 'atk', 'def', 'spa', 'spd', 'spe', 'abilitie1', 'abilitie2', 'abilitieH', 'tier', 'tierint',
                 'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground',
                 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water'])
    # Add new ROW
    poke = pokedex()
    i = 0
    for pokemon in poke:
        list = [poke[pokemon]['name'], poke[pokemon]['num'],
                poke[pokemon]['baseStats']['hp']*2+110, poke[pokemon]['baseStats']['atk']*2+5,
                poke[pokemon]['baseStats']['def']*2+5, poke[pokemon]['baseStats']['spa']*2+5,
                poke[pokemon]['baseStats']['spd']*2+5, poke[pokemon]['baseStats']['spe']*2+5,
                poke[pokemon]['abilities']['0'], poke[pokemon]['abilities']['1'],
                poke[pokemon]['abilities']['H'], switch(str(poke[pokemon]['tier'])), switch_int(str(poke[pokemon]['tier'])),
                type('Bug', poke[pokemon]), type('Dark', poke[pokemon]), type('Dragon', poke[pokemon]),
                type('Electric', poke[pokemon]), type('Fairy', poke[pokemon]), type('Fighting', poke[pokemon]),
                type('Fire', poke[pokemon]), type('Flying', poke[pokemon]), type('Ghost', poke[pokemon]),
                type('Grass', poke[pokemon]), type('Ground', poke[pokemon]), type('Ice', poke[pokemon]),
                type('Normal', poke[pokemon]), type('Poison', poke[pokemon]), type('Psychic', poke[pokemon]),
                type('Rock', poke[pokemon]), type('Steel', poke[pokemon]), type('Water', poke[pokemon]),
                ]
        df.loc[i] = list
        i = i + 1

    print(len(df))
    return df


def switch(argument):
    switcher = {
        'LC': 'weak',
        'NFE': 'weak',
        'RUBL': 'medium',
        'AG': 'strong',
        'PU': 'weak',
        'NU': 'medium',
        '(PU)': 'weak',
        'PUBL': 'weak',
        'UU': 'strong',
        'OU': 'strong',
        'UUBL': 'strong',
        'RU': 'medium',
        'Uber': 'strong',
        'NUBL': 'medium',
    }
    return switcher.get(argument)

def switch_int(argument):
    switcher = {
        'LC': 0,
        'NFE': 0,
        'RUBL': 1,
        'AG': 2,
        'PU': 0,
        'NU': 1,
        '(PU)': 0,
        'PUBL': 0,
        'UU': 2,
        'OU': 2,
        'UUBL': 2,
        'RU': 1,
        'Uber': 2,
        'NUBL': 1,
    }
    return switcher.get(argument)


def type(type, pok):
    res = 0
    if len(pok['types']) == 2:
        if pok['types'][1] == type:
            res = 1
    if pok['types'][0] == type or res == 1:
        return 1
    else:
        return 0


def poke_data_set():
    df = pokedex_df()
    feature_cols = ['hp', 'atk','spa',  'spe']
    return sklearn.utils.Bunch(data= (df[feature_cols].to_numpy()).astype('float'),  target_names=numpy.array(['weak' ,'medium', 'strong']), target=(df.tierint.to_numpy()).astype('int'), feature_names = feature_cols )


