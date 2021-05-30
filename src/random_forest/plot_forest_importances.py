import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

from CombinedScrapper.pokedex_to_df_ds import poke_data_set
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split


def plot_forest_importance():
    ds = poke_data_set()
    X, y, feature_names = ds.data, ds.target, ds.feature_names
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.30, random_state=42)

    # A random forest classifier will be fitted to compute the feature importances.
    from sklearn.ensemble import RandomForestClassifier

    forest = RandomForestClassifier(random_state=0, criterion="entropy", max_depth=5)
    forest.fit(X_train, y_train)

    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)

    forest_importance = pd.Series(importances, index=feature_names)

    fig, ax = plt.subplots()
    forest_importance.plot.bar(yerr=std, ax=ax)
    ax.set_title("Feature importances using MDI")
    ax.set_ylabel("Mean decrease in impurity")
    fig.tight_layout()

    result = permutation_importance(forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2)

    forest_importance = pd.Series(result.importances_mean, index=feature_names)

    fig, ax = plt.subplots()
    forest_importance.plot.bar(yerr=result.importances_std, ax=ax)
    ax.set_title("Feature importances using permutation on full model")
    ax.set_ylabel("Mean accuracy decrease")
    fig.tight_layout()
    plt.show()

plot_forest_importance()

