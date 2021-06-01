from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline

from CombinedScrapper.pokedex_to_df_ds import poke_data_set


def pca_accuracy():
    poke = poke_data_set()
    features, target = poke.data, poke.target

    # Make a train/test split using 30% test size
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.30, random_state=2)

    # Fit to data and predict using pipelined GNB and PCA.
    unscaled_clf = make_pipeline(PCA(n_components=4), GaussianNB())
    unscaled_clf.fit(X_train, y_train)
    pred_test = unscaled_clf.predict(X_test)

    # Fit to data and predict using pipelined scaling, GNB and PCA.
    std_clf = make_pipeline(StandardScaler(), PCA(n_components=4), GaussianNB())
    std_clf.fit(X_train, y_train)
    pred_test_std = std_clf.predict(X_test)

    # Show prediction accuracies in scaled and unscaled data.
    print("___PCA__NORMAL_DATASET___")
    print("Accuracy: ",metrics.accuracy_score(y_test, pred_test))
    print('\n')

    print("___PCA__STANDARDIZED_DATASET___")
    print("Accuracy:",metrics.accuracy_score(y_test, pred_test_std))
    print('\n')


def show_pca():
    poke = poke_data_set()
    features, target = poke.data, poke.target

    # Make a train/test split using 30% test size
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.30, random_state=42)

    # Fit to data and predict using pipelined GNB and PCA.
    unscaled_clf = make_pipeline(PCA(n_components=4), GaussianNB())
    unscaled_clf.fit(X_train, y_train)
    pred_test = unscaled_clf.predict(X_test)

    # Fit to data and predict using pipelined scaling, GNB and PCA.
    std_clf = make_pipeline(StandardScaler(), PCA(n_components=4), GaussianNB())
    std_clf.fit(X_train, y_train)

    # Extract PCA from pipeline
    pca = unscaled_clf.named_steps['pca']
    pca_std = std_clf.named_steps['pca']

    # Use PCA without and with scale on X_train data for visualization.
    X_train_transformed = pca.transform(X_train)
    scaler = std_clf.named_steps['standardscaler']
    X_train_std_transformed = pca_std.transform(scaler.transform(X_train))

    # visualize standardized vs. untouched dataset with PCA performed
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 7))

    class_names = ['weak', 'medium', 'strong']
    for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
        ax1.scatter(X_train_transformed[y_train == l, 0],
                    X_train_transformed[y_train == l, 1],
                    color=c,
                    label=class_names[l],
                    alpha=0.5,
                    marker=m
                    )

    for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
        ax2.scatter(X_train_std_transformed[y_train == l, 0],
                    X_train_std_transformed[y_train == l, 1],
                    color=c,
                    label=class_names[l],
                    alpha=0.5,
                    marker=m
                    )

    ax1.set_title('Training dataset after PCA')
    ax2.set_title('Standardized training dataset after PCA')

    for ax in (ax1, ax2):
        ax.set_xlabel('1st principal component')
        ax.set_ylabel('2nd principal component')
        ax.legend(loc='upper right')
        ax.grid()

    plt.tight_layout()
    plt.show()

def pca_predict(stats):
    poke = poke_data_set()
    features, target,  class_names = poke.data, poke.target, poke.target_names

    # Make a train/test split using 30% test size
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.01, random_state=2)

    # Fit to data and predict using pipelined GNB and PCA.
    unscaled_clf = make_pipeline(PCA(n_components=4), GaussianNB())
    unscaled_clf.fit(X_train, y_train)
    pred_test = unscaled_clf.predict([stats])

    # Fit to data and predict using pipelined scaling, GNB and PCA.
    std_clf = make_pipeline(StandardScaler(), PCA(n_components=4), GaussianNB())
    std_clf.fit(X_train, y_train)
    pred_test_std = std_clf.predict([stats])

    # Show prediction accuracies in scaled and unscaled data.
    print("___PCA__NORMAL_DATASET___")
    print("Prediction: ", class_names[pred_test[0]])
    print('\n')

    print("___PCA__STANDARDIZED_DATASET___")
    print("Prediction: ", class_names[pred_test_std[0]])
    print('\n')