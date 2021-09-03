# 조선왕들의 평균 나이
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm
# Boston = sm.datasets.get_rdataset("Boston", package="MASS")['data']
# get_rdataset은 R에 있는 데이터셋을 불러와 사용할 수 있는 함수 즉 R안에 있는 boston 데이터 셋을 불러온다.

kings = pd.read_csv("/Users/hamjimin/Desktop/DS_Python_ex_vis/chosun_kings.csv", encoding="euc-kr")
type(kings)
kings.head()
kings.shape

# 평균 수명의 나이를 받아오기
from matplotlib.figure import figaspect
w, h = figaspect(0.6)
fig, ax = plt.subplots(figsize=(w,h))
plt.hist(kings.life, bins=range(0,100,10))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title("Chosun Kings", size=25)
plt.xlabel("Life Years", size=20)
plt.show()