# k-mean clustering, boston data
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections as cl
from sklearn import preprocessing
import seaborn as sns

Boston = pd.read_csv("/Users/hamjimin/Desktop/DS_Python_ex_vis/Boston.csv")
X = Boston.drop("medv", axis=1)

names = X.columns
scaler = preprocessing.StandardScaler()
scaled_X = scaler.fit_transform(X)
scaled_X = pd.DataFrame(scaled_X, columns=names)

kmeans = KMeans(n_clusters=4, random_state=0).fit(scaled_X)
kmeans.labels_
cl.Counter(kmeans.labels_)
# Counter ({1:233, 3:88, 2:151, 0:34})
# 가장 큰 군집은 1번 군집, 가장 작은 군집은 군집 0  <- 군집의 크기


centers = kmeans.cluster_centers_[:,[0,4,5,6,7,12]].round(2)
print(pd.DataFrame(centers, columns=X.columns[[0,4,5,6,7,12]])) # 군집의 중심

#    crim   nox    rm   age   dis  lstat
# 0 -0.20  0.38  0.28  0.37 -0.40  -0.16
# 1 -0.38 -0.34  0.06 -0.07  0.06  -0.26
# 2  0.86  1.07 -0.50  0.80 -0.85   0.95
# 3 -0.41 -1.14  0.63 -1.38  1.51  -0.91

# 군집 특성 포착


#box plot 을 보고싶지만 sns을 켜는 방법을 모르겟다.
sns.boxplot(x = kmeans.labels_, y= Boston.medv).set(xlabel='cluster', aspect=0.075)