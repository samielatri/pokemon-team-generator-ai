#!/usr/bin/env python
# coding: utf-8

def bayes():
    # In[1]:


    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import confusion_matrix, classification_report
    import statsmodels.api as sm
    from statsmodels.formula.api import glm
    sns.set_theme()


    # In[3]:


    dataset1 = pd.read_csv('Pokemon.csv', index_col=0)

    dataset = pd.concat([(dataset1.loc[dataset1['tier'] == 'weak'  ])[:130],
                         (dataset1.loc[dataset1['tier'] == 'medium'])[:120],
                         (dataset1.loc[dataset1['tier'] == 'strong'])[:120]])

    dataset.loc[:, 'tier'] = dataset.loc[:, 'tier'].astype('category')
    dic = {'weak':1, 'medium':2, 'strong':3}
    dataset.loc[:,'tier1'] = [dic[i] for i in dataset[['tier']].values.ravel()]


    # ### Visualization

    # #### Correlation of Variables

    # In[4]:


    dataset.corr()[['tier1']]


    # #### BoxPlot Graphs of highly correlated variables

    # In[5]:


    f, axes = plt.subplots(3, 3, figsize = (15,10))
    sns.boxplot(y="hp" , x= "tier", data = dataset , ax=axes[0][0])
    sns.boxplot(y="atk", x= "tier", data = dataset , ax=axes[0][1])
    sns.boxplot(y="spa", x= "tier", data = dataset , ax=axes[0][2])
    sns.boxplot(y="spd", x= "tier", data = dataset , ax=axes[1][0])
    sns.boxplot(y="spe", x= "tier", data = dataset , ax=axes[1][1])
    sns.boxplot(y="def", x= "tier", data = dataset , ax=axes[1][2])
    sns.scatterplot(y="hp", x= "atk", data = dataset , ax=axes[2][2], hue="tier")
    sns.scatterplot(y="def", x= "atk", data = dataset , ax=axes[2][1], hue="tier")
    sns.histplot(dataset.tier, ax=axes[2][0])


    # In[6]:


    ## Create Radar Plot to check average values of the features of the different classes

    from math import pi
    # Set data
    df = pd.DataFrame([np.mean(dataset.loc[dataset['tier'] == 'weak']), 
                  np.mean(dataset.loc[dataset['tier'] == 'medium']),
                  np.mean(dataset.loc[dataset['tier'] == 'strong'])], index=['weak','medium','strong']).iloc[:, 1:7]
    # ------- PART 1: Create background

    # number of variable
    categories=list(df)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    f, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, size=12)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([60,70,80,90, 100, 110], ["60","70","80","90","100", "110"], color="grey", size=12)
    plt.ylim(0,120)


    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

    for i in df.index:
        values=df.loc[i].values.flatten().tolist()
        values+=values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=i)
        ax.fill(angles, values, alpha=0.1)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    df


    # ## Classification
    # ### Naive Bayes Classifier

    # In[33]:


    ## Using only the highly correlated variables
    X = dataset[['hp', 'atk','spa', 'spd']]
    y = dataset[['tier']].astype('category').values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)


    # In[34]:


    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)


    # In[35]:


    acc = sum((y_pred==y_test).astype('float'))/len(((y_pred==y_test).astype('float')))
    confmat = (confusion_matrix(y_test, y_pred,labels=['weak','medium','strong'])) 
    print("accuracy = ", acc)
    pd.DataFrame(confmat, columns=['weak','medium','strong'], index=['weak','medium','strong'])


    # In[36]:


    ## Normalized Confusion Matrix showing percentage of correct predictions per class
    pd.DataFrame([np.divide(i,np.sum(i)) for i in confmat], columns=['weak','medium','strong'], index=['weak','medium','strong'])

    return (X_train, y_train, X_test, y_test)

def neural_networks(X_train, y_train, X_test, y_test):
    # ### Neural Networks

    # #### Linear Perceptron (Single Layer Perceptron)

    # In[43]:


    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import StandardScaler  
    from sklearn.linear_model import Perceptron
    scaler = StandardScaler().fit(X_train)
    X_train_ = scaler.transform(X_train)  
    # apply same transformation to test data
    X_test_ = scaler.transform(X_test)


    # In[83]:


    clf = Perceptron(tol=1e-5, class_weight='balanced', penalty='l2', shuffle=True, verbose=True)
    clf.fit(X_train_, y_train)
    clf.score(X_test_, y_test)
    y_pred = clf.predict(X_test_)


    # In[84]:


    acc = sum((y_pred==y_test).astype('float'))/len(((y_pred==y_test).astype('float')))
    confmat = (confusion_matrix(y_test, y_pred,labels=['weak','medium','strong'])) 
    print("accuracy = ", acc)
    pd.DataFrame(confmat, columns=['weak','medium','strong'], index=['weak','medium','strong'])


    # In[85]:


    ## Normalized Confusion Matrix showing percentage of correct predictions per class
    pd.DataFrame([np.divide(i,np.sum(i)) for i in confmat], columns=['weak','medium','strong'], index=['weak','medium','strong'])


    # #### MultiLayer Perceptron Classifier

    # In[113]:


    clf = MLPClassifier(random_state=10,solver='sgd',activation='identity', batch_size=4, power_t=0.7, verbose=True, tol=0.9)
    clf.fit(X_train_, y_train)
    y_pred = clf.predict(X_test_)
    clf.score(X_test_, y_test)


    # In[114]:


    acc = sum((y_pred==y_test).astype('float'))/len(((y_pred==y_test).astype('float')))
    confmat = (confusion_matrix(y_test, y_pred,labels=['weak','medium','strong'])) 
    print("accuracy = ", acc)
    pd.DataFrame(confmat, columns=['weak','medium','strong'], index=['weak','medium','strong'])


    # In[115]:


    ## Normalized Confusion Matrix showing percentage of correct predictions per class
    pd.DataFrame([np.divide(i,np.sum(i)) for i in confmat], columns=['weak','medium','strong'], index=['weak','medium','strong'])

#functions call
X_train, y_train, X_test, y_test = bayes()
neural_networks(X_train, y_train, X_test, y_test)

# ### Conclusion
# 1. Class Imbalance was a big problem for predictions. Therefore undersampling was used to balance the data.
# 2. From the Radar Plot, it is evident that the feature means are very close for medium and strong classes, while difference between feature means of weak and medium is higher. Which is a reason behind most of medium tiers being classified as strong. 
# 2. All of the methods seemed to be giving a good accuracy for Strong and Weak Classes as they had more data. Medium Tier had very less data and thus had a lower accuracy.
# 3. Naive Bayes Classifier had a good overall performance, with good predictions on Weak Tier as well.
# 4. Linear Perceptron and MultiLayer Perceptron had high accuracies on Weak and Strong Classes, but very less accuracy on Medium.

# In[ ]:
