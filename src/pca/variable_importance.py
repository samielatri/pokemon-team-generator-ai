#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from CombinedScrapper.pokedex_to_df_ds import poke_data_set, pokedex_df


def myplot(score, coeff, labels, num, y):
    xs = score[:, 0]
    ys = score[:, 1]
    n = coeff.shape[0]
    scalex = 1.0 / (xs.max() - xs.min())
    scaley = 1.0 / (ys.max() - ys.min())
    plt.scatter(xs * scalex, ys * scaley, c=y)
    for i in range(n):
        plt.arrow(0, 0, coeff[i, 0], coeff[i, 1], color='#185F8C', alpha=0.5)
        plt.text(coeff[i, 0] * 1.1, coeff[i, 1] * 1.1, labels[i], color='#185F8C', ha='center', va='center')
    i = 0
    for x, y2 in zip(xs * scalex, ys * scaley):
        plt.annotate(num[i],  # this is the text
                     (x, y2),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 5),  # distance from text to points (x,y)
                     ha='center',
                     fontsize=6)  # horizontal alignment can be left, right or center
        i = i + 1


def variable_importance():
    poke = poke_data_set()
    X, y = poke.data, poke.target
    y = y.astype('int')
    labels = poke.feature_names
    # In general a good idea is to scale the data
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    df = pokedex_df()
    num = df['num']
    pca = PCA()
    x_new = pca.fit_transform(X)

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()

    # Call the function. Use only the 2 PCs.
    myplot(x_new[:, 0:2], np.transpose(pca.components_[0:2, :]), labels, num, y)
    plt.show()
