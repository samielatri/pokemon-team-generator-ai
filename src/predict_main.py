#!/usr/bin/env python
# coding: utf-8
from CombinedScrapper.pokedex_to_df_ds import poke_level_100
from knn.knn import knn_predict
from pca.standarized_dt_pca import pca_predict
from random_forest.random_forest import random_forest_predict
from tree_learning.tree_learning import tree_learning_predict

hp = int(input("Entrez la statistique hp : "))
atk = int(input("Entrez la statistique atk : "))
spa = int(input("Entrez la statistique spa : "))
spd = int(input("Entrez la statistique spd : "))

stats = poke_level_100([hp, atk, spa, spd])
print("Les statistiques de votre pokémon au niveau 100 (sans EV et IV) : ", stats)
print("Estimation de la puissance de votre pokémon : \n ... chargement...")
tree_learning_predict(stats)
random_forest_predict(stats)
pca_predict(stats)
knn_predict(stats)
