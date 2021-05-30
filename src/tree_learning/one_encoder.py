#!/usr/bin/env python
# coding: utf-8

# In[1]:
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
from CombinedScrapper.pokedex_to_df_ds import pokedex_df

def one_encoder_accuracy():
    df = pokedex_df()
    le = LabelEncoder()
    df['abilitie1'] = LabelEncoder().fit_transform(df['abilitie1'])
    df['abilitie2'] = LabelEncoder().fit_transform(df['abilitie2'])
    df['abilitieH'] = LabelEncoder().fit_transform(df['abilitieH'])

    # split dataset in features and target variable
    feature_cols = ['hp', 'atk', 'def', 'spa', 'spd', 'spe',
                    'abilitie1', 'abilitie2', 'abilitieH', 'Bug', 'Dark', 'Dragon',
                    'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground',
                    'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
    X = df[feature_cols]  # Features
    y = df.tier  # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("___TREE_LEARNING__ENTROPY_MAX_DEPTH=5__OneEncoder___")
    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    print('\n')
