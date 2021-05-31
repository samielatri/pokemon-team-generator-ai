# coding: utf-8

# Implémentation de K-means clustering python
# Code produit par le site https://mrmint.fr

#Chargement des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from team_generator.set_generator import clustering_set, usage_to_df
from sklearn import datasets


#chargement de jeu des données Iris

def clustering_label():
    poke = clustering_set()


    #importer le jeu de données Iris dataset à l'aide du module pandas
    x = pd.DataFrame(poke.data)

    x.columns = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']

    #Création d'un objet K-Means avec un regroupement en 3 clusters (groupes)
    model=KMeans(n_clusters=3)

    #application du modèle sur notre jeu de données Iris
    model.fit(x)

    return model.labels_

def show_clustering() :
    poke = clustering_set()
    label = usage_to_df()
    label = label['Name']

    # importer le jeu de données Iris dataset à l'aide du module pandas
    x = pd.DataFrame(poke.data)

    x.columns = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
    labels_ = clustering_label()
    colormap = np.array(['Red', 'green', 'blue'])
    print(labels_)

    # Visualisation des clusters formés par K-Means
    plt.scatter(x.spe, x.atk, c=colormap[labels_], s=40)
    i = 0
    while i < len(label):
        plt.text(x.spe[i], x.atk[i], label[i],
                 fontsize=10)
        i = i + 1

    plt.title('Classification K-means ')
    plt.show()

show_clustering()


