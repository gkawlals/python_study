import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from matplotlib.figure import figaspect
# 동물의 몸무게와 뇌의 무게를 비교하는 산점도를 나타내라
# 에러발생 get_rdataset의 대한 에러가 발생

mammals = sm.datasets.get_rdataset("mammals", package="MASS")['data']
mammals.head(5)

w,h = figaspect(1)
plt.scatter(mammals.bovy, mammals.brain)
plt.title("mammals", fontsize=25)
plt.xlabel("body", fontsize=20)
plt.ylabel("body", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

