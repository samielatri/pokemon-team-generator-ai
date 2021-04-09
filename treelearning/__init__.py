#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder

from pokedexGenerator.generator import pokedex_df

df = pokedex_df()

le = LabelEncoder()
df['type1']= LabelEncoder().fit_transform(df['type1'])
df['type2']= LabelEncoder().fit_transform(df['type2'])
df['abilitie1']= LabelEncoder().fit_transform(df['abilitie1'])
df['abilitie2']= LabelEncoder().fit_transform(df['abilitie2'])
df['abilitieH']= LabelEncoder().fit_transform(df['abilitieH'])
#split dataset in features and target variable
feature_cols = ['type1', 'type2', 'hp', 'atk', 'def', 'spa', 'spd', 'spe','abilitie1', 'abilitie2', 'abilitieH']
X = df[feature_cols] # Features
y = df.tier # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# # Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# # Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

# #Predict the response for test dataset
y_pred = clf.predict(X_test)
#
# # Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))