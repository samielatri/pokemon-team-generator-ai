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
    list_team = teammates(f'export_poke.csv', pokemon)
    dex = dex.assign(Cluster=label_clustering)

    # ADD THE SECOND POKEMON
    pokemon = list_team[0]
    pokemon_list.append(pokemon)

    # ADD THE THIRD POKEMON
    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])

    for index, row in dex.iterrows():
        if not row['Cluster'] in list_label:
            if not row["Name"] in pokemon_list:
                pokemon_list.append(row["Name"])
                break

    # ADD THE FOURTH POKEMON
    list_team = teammates(f'export_poke.csv', pokemon_list[2])
    for p in list_team:
        if not p in pokemon_list:
            pokemon_list.append(p)
            break

    # ADD THE FIFTH
    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])
    set_pokemon = set(list_label)
    if len(set_pokemon) < 3 :
        for index, row in dex.iterrows():
            if not row['Cluster'] in list_label:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break
    elif sum(list_label) == 3:
        for index, row in dex.iterrows():
            if row['Cluster'] == 1:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break
    elif sum(list_label) == 4:
        for index, row in dex.iterrows():
            if row['Cluster'] == 2:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break
    elif sum(list_label) == 5:
        for index, row in dex.iterrows():
            if row['Cluster'] == 0:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break

    #ADD THE SIXTH POKEMON
    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])
    if list_label[4] == 2:
        for index, row in dex.iterrows():
            if row['Cluster'] == 0:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break
    elif list_label[4] == 1:
        for index, row in dex.iterrows():
            if row['Cluster'] == 2:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break
    elif list_label[4] == 0:
        for index, row in dex.iterrows():
            if row['Cluster'] == 1:
                if not row["Name"] in pokemon_list:
                    pokemon_list.append(row["Name"])
                    break


    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])
    list_team = teammates(f'export_poke.csv', pokemon_list[4])
    for p in list_team:
        if not p in pokemon_list and len(pokemon_list) < 6:
            for index, row in dex.iterrows():
                if p == row['Name'] :
                    if row["Cluster"] != list_label[4]:
                        pokemon_list.append(p)
                        break

    list_label = []
    for p in pokemon_list:
        for index, row in dex.iterrows():
            if row["Name"] == p:
                list_label.append(row['Cluster'])
    print(list_label)
    print(pokemon_list)
    print(to_pokepaste('gen8ou', pokemon_list))

team_generator('Landorus-Therian')
