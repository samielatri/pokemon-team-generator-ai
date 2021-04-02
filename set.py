#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json

import httplib2


# http = httplib2.Http()
# status, response = http.request('https://play.pokemonshowdown.com/data/sets/gen8ou.json')
#
# todos = json.loads(response)
#
# print(todos['dex']["Venusaur"])
#
# json.dumps(todos)


def pokemon_to_pokepaste(dex, pokemon):
    pokemon_set = dex['dex'][pokemon]
    for i in pokemon_set:
        set_name = i
    pokemon_paste = pokemon + ' @ ' + pokemon_set[set_name]['item'] + '\n'\
                    + 'Ability: ' + pokemon_set[set_name]['ability'] + '\n' \
                    + 'Level: 50\nEVs: ' \
                    + str(pokemon_set[set_name]['evs'].get('hp', 0)) + ' HP / ' \
                    + str(pokemon_set[set_name]['evs'].get('def', 0)) + ' Def / ' \
                    + str(pokemon_set[set_name]['evs'].get('spa', 0)) + ' SpA / ' \
                    + str(pokemon_set[set_name]['evs'].get('spd', 0)) + ' SpD / ' \
                    + str(pokemon_set[set_name]['evs'].get('spe', 0)) + ' Spe \n' \
                    + pokemon_set[set_name]['nature'] + "Nature\n"
    for i in pokemon_set[set_name]['moves'] :
        pokemon_paste = pokemon_paste + "- " + i + "\n"
    return pokemon_paste


def to_pokepaste(tier, pokemon):
    http = httplib2.Http()
    status, response = http.request(f'https://play.pokemonshowdown.com/data/sets/{tier}.json')
    dex = json.loads(response)
    pokepaste = ""
    for i in pokemon:
        pokepaste = pokepaste + pokemon_to_pokepaste(dex, i) + '\n\n'
    return pokepaste


print(to_pokepaste('gen8ou', ["Venusaur", "Charizard", "Clefable", "Ninetales-Alola", "Slowbro", "Gengar"]))
fichier = open("data.txt", "a")
fichier.write(to_pokepaste('gen8ou', ["Venusaur", "Charizard", "Clefable", "Ninetales-Alola", "Slowbro", "Gengar"]))
fichier.close()
