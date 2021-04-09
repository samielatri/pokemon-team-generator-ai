#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json

import httplib2
import pandas as pd


def pokedex():
    http = httplib2.Http()
    status, response = http.request(f'https://play.pokemonshowdown.com/data/pokedex.json')
    pokedex = json.loads(response)
    list_pokemon = []
    # for pokemon in pokedex:
    #     if pokedex[pokemon]['num'] > 151:
    #         list_pokemon.append(pokemon)

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
    df = pd.DataFrame(columns=['Name', 'num', 'type1', 'type2', 'hp', 'atk', 'def', 'spa', 'spd', 'spe', 'abilitie1', 'abilitie2', 'abilitieH','tier'])
    # Add new ROW
    poke = pokedex()
    i = 0
    for pokemon in poke:
        list = [poke[pokemon]['name'], poke[pokemon]['num'], poke[pokemon]['types'][0],
                len(poke[pokemon]['types'])==1 if 'none'else poke[pokemon]['types'][0],
                poke[pokemon]['baseStats']['hp'], poke[pokemon]['baseStats']['atk'],
                poke[pokemon]['baseStats']['def'], poke[pokemon]['baseStats']['spa'],
                poke[pokemon]['baseStats']['spd'], poke[pokemon]['baseStats']['spe'],
                poke[pokemon]['abilities']['0'], poke[pokemon]['abilities']['1'],
                poke[pokemon]['abilities']['H'],
                switch(str(poke[pokemon]['tier']))]
        df.loc[i] = list
        i = i + 1

    print(len(df))
    return df


def switch(argument):
    switcher = {
        'LC':'weak',
        'NFE':'weak',
        'RUBL':'medium',
        'AG':'strong',
        'PU':'weak',
        'NU':'medium',
        '(PU)':'weak',
        'PUBL':'weak',
        'UU':'strong',
        'OU':'strong',
        'UUBL':'strong',
        'RU':'medium',
        'Uber':'strong',
        'NUBL':'medium',
    }
    return switcher.get(argument)
