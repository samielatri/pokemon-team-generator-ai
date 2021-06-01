#!/usr/bin/env python
# coding: utf-8

# In[1]:
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

from CombinedScrapper.pokedex_to_df_ds import pokedex_df

def knn_accuracy():
    df = pokedex_df()

    feature_cols = ['hp', 'atk',  'spa', 'spd']
    X = df[feature_cols] # Features
    y = df.tier # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y.astype(str), test_size=0.30, random_state=42) # 70% training and 30% test

    knn = KNeighborsClassifier(n_neighbors=10)

    #Train the model using the training sets
    knn.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = knn.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("___KNN___n_neighbors=10___")
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print('\n')




def predict_knn(stat) :
    df = pokedex_df()

    feature_cols = ['atk', 'def', 'spa', 'spd']
    X = df[feature_cols] # Features
    y = df.tier # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y.astype(str), test_size=0.01, random_state=42) # 70% training and 30% test

    knn = KNeighborsClassifier(n_neighbors=10)

    #Train the model using the training sets
    knn.fit(X_train, y_train)

    #Predict the response for test dataset
    predict = knn.predict([stat])
    return predict