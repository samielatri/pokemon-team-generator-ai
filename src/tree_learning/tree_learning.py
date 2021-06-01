#!/usr/bin/env python
# coding: utf-8

from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

from CombinedScrapper.pokedex_to_df_ds import poke_data_set


def tree_learning_accuracy():
    # split dataset in features and target variable
    ds = poke_data_set()
    X, y, class_names, feature_cols = ds.data, ds.target, ds.target_names, ds.feature_names

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=42)  # 70% training and 30% test

    # Create Decision Tree classifer object and train it
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("___TREE_LEARNING___")
    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    print('\n')

    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("___TREE_LEARNING__ENTROPY_MAX_DEPTH=5___")
    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    print('\n')


def draw_tree():
    # split dataset in features and target variable
    ds = poke_data_set()
    X, y, class_names, feature_cols = ds.data, ds.target, ds.target_names, ds.feature_names

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_cols, class_names=['weak', 'medium', 'strong'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('tiers.png')
    Image(graph.create_png())


def tree_learning_predict(stats):
    # split dataset in features and target variable
    ds = poke_data_set()
    X, y, class_names, feature_cols = ds.data, ds.target, ds.target_names, ds.feature_names

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01,
                                                        random_state=42)  # 70% training and 30% test

    # Create Decision Tree classifer object and train it
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict([stats])

    print("___TREE_LEARNING___")
    print("Prediction: ", class_names[y_pred[0]])
    print('\n')

    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict([stats])

    print("___TREE_LEARNING__ENTROPY_MAX_DEPTH=5___")
    print("Prediction: ", class_names[y_pred[0]])
    print('\n')
