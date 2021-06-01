#!/usr/bin/env python
# coding: utf-8
import pandas as pd

from team_generator.set_generator import usage_to_df
from team_generator.team_generator_final import team_generator

df = usage_to_df()
list_poke = df['Name'].tolist()
i = 0
for poke in list_poke :
    print(str(i) + " - " + str(poke))
    i = i + 1

num = input("Sur quel Pokémon voulez-vous baser votre team ? (entrez son numéro) ")
print("Génération de la team ...")
team_generator(list_poke[int(num)])