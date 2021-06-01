import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

# import some data to play with
from sklearn.tree import DecisionTreeClassifier

from CombinedScrapper.pokedex_to_df_ds import poke_data_set

def confusion_matrix():
    ds = poke_data_set()
    X, y, class_names,  = ds.data, ds.target, ds.target_names

    # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70% training and 30% test


    # Run classifier, using a model that is too regularized (C too low) to see
    # the impact on the results
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5).fit(X_train,y_train)

    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    titles_options = [("Confusion matrix, without normalization", None),
                      ("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(clf, X_test, y_test,
                                     display_labels=class_names,
                                     cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

    plt.show()
