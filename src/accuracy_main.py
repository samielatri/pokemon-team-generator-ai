#!/usr/bin/env python
# coding: utf-8
from knn.knn import knn_accuracy
from pca.standarized_dt_pca import pca_accuracy
from random_forest.random_forest import random_forest_accuracy
from tree_learning.tree_learning import tree_learning_accuracy

tree_learning_accuracy()
random_forest_accuracy()
knn_accuracy()
pca_accuracy()