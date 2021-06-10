#!/usr/bin/env python
# coding: utf-8
from CombinedScrapper.set_scrap import teammates
from team_generator.clustering import clustering_label
from team_generator.pokepaste_generator import to_pokepaste
from team_generator.set_generator import usage_to_df


def team_generator(pokemon):
    pokemon_list = [pokemon]

    label_clustering = clustering_label()
    dex = usage_to_df()
    dex = dex.assign(Cluster=label_clustering)

    # ADD THE SECOND POKEMON
    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])
    list_team = teammates(f'output/export_poke.csv', pokemon_list[0])
    for p in list_team:
        if not p in pokemon_list and len(pokemon_list) < 2:
            for index, row in dex.iterrows():
                if p == row['Name'] and row["Cluster"] != list_label[0]:
                    pokemon_list.append(p)
                    break

    # ADD THE THIRD POKEMON
    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])

    for index, row in dex.iterrows():
        if not row['Cluster'] in list_label and not row["Name"] in pokemon_list:
            pokemon_list.append(row["Name"])
            break

    # ADD THE FOURTH POKEMON
    list_team = teammates(f'output/export_poke.csv', pokemon_list[2])
    for p in list_team:
        if not p in pokemon_list and len(pokemon_list) < 4:
            for index, row in dex.iterrows():
                if p == row['Name']:
                    pokemon_list.append(p)
                    break

    # ADD THE FIFTH POKEMON
    list_label = []
    for index, row in dex.iterrows():
        if row["Name"] == pokemon_list[3]:
            list_label.append(row['Cluster'])
            break
    list_team = teammates(f'output/export_poke.csv', pokemon_list[3])
    for p in list_team:
        if not p in pokemon_list and len(pokemon_list) < 5:
            for index, row in dex.iterrows():
                if p == row['Name'] and row["Cluster"] != list_label[0]:
                    pokemon_list.append(p)
                    break

    # ADD THE SIXTH POKEMON
    list_label = []
    i = 3
    while i < 5:
        for index, row in dex.iterrows():
            if row["Name"] == pokemon_list[i]:
                list_label.append(row['Cluster'])
        i = i + 1
    list_team = teammates(f'output/export_poke.csv', pokemon_list[4])
    for p in list_team:
        if not p in pokemon_list and len(pokemon_list) < 6:
            for index, row in dex.iterrows():
                if p == row['Name'] and not row['Cluster'] in list_label:
                    pokemon_list.append(p)
                    break
    while len(pokemon_list) < 6:
        for index, row in dex.iterrows():
            if not row['Cluster'] in list_label and not row["Name"] in pokemon_list:
                pokemon_list.append(row["Name"])
                break

    print(to_pokepaste('gen8ou', pokemon_list))
