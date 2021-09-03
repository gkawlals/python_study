# 차(수치형), 보스턴(범주형)의 주택가격의 대한 분포표
# 산점도(수치형)와 박스형태(범주형)의 그래프로 나타내라

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from matplotlib.figure import figaspect
# 수치형인 cars의 대한 정보를 cars.csv파일에서 불러오기
cars = pd.read_csv("/Users/hamjimin/Desktop/DS_Python_ex_vis/cars.csv")
plt.scatter(cars.speed, cars.dist).axes.set_aspect(0.18)
plt.title("cars", fontsize=25)
plt.xlabel("speed", fontsize=20)
plt.ylabel("distance", fontsize=20)
plt.show()
# 범주형인 Boston
Boston = sm.datasets.get_rdataset("Boston", package="MASS")['data']
cut = np.median(Boston.dis)
dgr = (Boston.dis >= cut)
sns.set(font_scale=2)
sns.boxplot(x = dgr, y = Boston.medv).set(xlabel = 'distance', ylabel = 'price',aspect=0.075 , title="Boston")


