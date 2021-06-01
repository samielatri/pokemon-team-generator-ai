#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json

import httplib2


#Prends un dico et le nom d'un pokémon et donne son set compatible avec smogon
def pokemon_to_pokepaste(dex, pokemon):
    pokemon_set = dex['dex'][pokemon]
    for i in pokemon_set:
        set_name = i
    pokemon_paste = pokemon + ' @ ' + pokemon_set[set_name]['item'] + '\n'\
                    + 'Ability: ' + pokemon_set[set_name]['ability'] + '\n' \
                    + 'Level: 100\nEVs: ' \
                    + str(pokemon_set[set_name]['evs'].get('hp', 0)) + ' HP / ' \
                    + str(pokemon_set[set_name]['evs'].get('def', 0)) + ' Def / ' \
                    + str(pokemon_set[set_name]['evs'].get('spa', 0)) + ' SpA / ' \
                    + str(pokemon_set[set_name]['evs'].get('spd', 0)) + ' SpD / ' \
                    + str(pokemon_set[set_name]['evs'].get('spe', 0)) + ' Spe \n' \
                    + pokemon_set[set_name]['nature'] + "Nature\n"
    for i in pokemon_set[set_name]['moves'] :
        pokemon_paste = pokemon_paste + "- " + i + "\n"
    return pokemon_paste


#Prends un tier et une liste de pokémon et donne leurs set compatible avec smogon
def to_pokepaste(tier, pokemon):
    http = httplib2.Http()
    status, response = http.request(f'https://play.pokemonshowdown.com/data/sets/{tier}.json')
    dex = json.loads(response)
    pokepaste = ""
    for i in pokemon:
        pokepaste = pokepaste + pokemon_to_pokepaste(dex, i) + '\n\n'
    return pokepaste

