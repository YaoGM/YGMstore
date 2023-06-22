import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

standard = np.load('standard.npz')['arr_0']
k = 3
kmeans_model = KMeans(n_clusters=k, n_init=3, random_state=123)
fit_kmeans = kmeans_model.fit(standard)
print('聚类中心: \n', kmeans_model.cluster_centers_)

print('样本的类别标签: \n', kmeans_model.labels_)

r1 = pd.Series(kmeans_model.labels_).value_counts()
print('最终每个类别的数目为： \n', r1)
