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
plt.ioff()
plt.scatter(cars.speed, cars.dist).axes.set_aspect(0.18)
m, d = np.polyfit(cars.speed, cars.dist, 1)
plt.plot(cars.speed,m * cars.dist + 1)
plt.title("cars", fontsize=25)
plt.xlabel("speed", fontsize=20)
plt.ylabel("distance", fontsize=20)
plt.show()
# lowess의 대한 에러가 발생 곡선으로 분포표를 가로질러 나와야함
plt.ioff()
fig = plt.scatter(cars.speed, cars.dist).axes.set_aspect(0.18)
curve = lowess(cars.dist, cars.speed, frac=0.6)
plt.plot(curve[:,0], curve[:1], 'blue', linewidth=1)
plt.show()