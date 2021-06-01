#!/usr/bin/env python
# coding: utf-8
from sklearn import metrics
from sklearn.model_selection import train_test_split

from CombinedScrapper.pokedex_to_df_ds import poke_data_set


def random_forest_accuracy():
    ds = poke_data_set()
    X, y, feature_names = ds.data, ds.target, ds.feature_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    # A random forest classifier will be fitted to compute the feature importances.
    from sklearn.ensemble import RandomForestClassifier

    forest = RandomForestClassifier(random_state=0, criterion="entropy", max_depth=5)
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)

    print("___RANDOM_FOREST_ENTROPY_MAX_DEPTH=5__")
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    print('\n')


def random_forest_predict(stats):
    ds = poke_data_set()
    X, y, feature_names, class_names = ds.data, ds.target, ds.feature_names, ds.target_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    # A random forest classifier will be fitted to compute the feature importances.
    from sklearn.ensemble import RandomForestClassifier

    forest = RandomForestClassifier(random_state=0, criterion="entropy", max_depth=5)
    forest.fit(X_train, y_train)
    y_pred = forest.predict([stats])

    print("___RANDOM_FOREST_ENTROPY_MAX_DEPTH=5__")
    print("Prediction: ", class_names[y_pred[0]])
    print('\n')
