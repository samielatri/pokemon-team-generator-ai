#!/usr/bin/env python
# coding: utf-8

# In[1]:
# matrice de confusion
#some de monoclassifier
#multi label
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.preprocessing import LabelEncoder
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

from pokedexGenerator.generator import pokedex_df
df = pokedex_df()

print(df['tier'].unique())
print(df['tier'].value_counts())


# le = LabelEncoder()
# df['type1']= LabelEncoder().fit_transform(df['type1'])
# df['type2']= LabelEncoder().fit_transform(df['type2'])
# df['abilitie1']= LabelEncoder().fit_transform(df['abilitie1'])
# df['abilitie2']= LabelEncoder().fit_transform(df['abilitie2'])
# df['abilitieH']= LabelEncoder().fit_transform(df['abilitieH'])
#split dataset in features and target variable
feature_cols = ['hp', 'atk', 'def', 'spa', 'spd', 'spe', 'Bug', 'Dark', 'Dragon', 'Electric',
                'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground',
                 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
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
#print('Confusion matrix : ', confusion_matrix(y_test, y_pred))

# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=['medium','strong','weak'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tiers.png')
Image(graph.create_png())