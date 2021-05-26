#!/usr/bin/env python
# coding: utf-8

# In[1]:
# matrice de confusion
#some de monoclassifier
#multi label
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

from CombinedScrapper.generator import pokedex_df

print('test')

df = pokedex_df()
del df['abilitie1']
del df['abilitie2']
del df['abilitieH']

print(df['tier'].unique())
print(df['tier'].value_counts())

#enc = OneHotEncoder(handle_unknown='ignore')

# enc_df = pd.DataFrame(enc.fit_transform(df[['type1']]).toarray())
# df = df.join(enc_df)

df = pd.get_dummies(df, prefix=['type1', 'type2'], columns=['type1', 'type2'])
print(df)
print(list(df))
feature_cols = ['num', 'hp', 'atk', 'def', 'spa', 'spd', 'spe', 'type1_Bug', 'type1_Dark', 'type1_Dragon', 'type1_Electric', 'type1_Fairy', 'type1_Fighting', 'type1_Fire', 'type1_Flying', 'type1_Ghost', 'type1_Grass', 'type1_Ground', 'type1_Ice', 'type1_Normal', 'type1_Poison', 'type1_Psychic', 'type1_Rock', 'type1_Steel', 'type1_Water', 'type2_False', 'type2_True']
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
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=['medium','strong','weak'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tiers.png')
Image(graph.create_png())