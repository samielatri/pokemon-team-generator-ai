from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

from CombinedScrapper.generator import poke_data_set

poke = poke_data_set()
pca = PCA(2)  # project from 64 to 2 dimensions
projected = pca.fit_transform(poke.data)
print(poke.data.shape)
print(projected.shape)

fig, ax = plt.subplots()
plt.scatter(projected[:, 0], projected[:, 1],
            c=poke.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Blues', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();
fig.tight_layout()
plt.show()