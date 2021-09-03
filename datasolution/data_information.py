import pandas as pd
import numpy as np
import statsmodels.api as sm

# subset Selection in Python - Smith College
# http://www.science.smith.edu/~jcrouser/SDS293/lavs/lab8-py.html <- 데이터셋을 불러다 사용할 수 있는 사이트

Hitters = sm.datasets.get_rdataset("Hitters",package="ISLR")['data']
Hitters.columns

Hitters.iloc[:,13].value_counts()

clmn = pd.get_dummies(Hitters["League"])["A"]

y = np.asarray(Hitters["Salary"])
indices = pd.notna(y)
y1 = y[indices]
y1.shape
X = np.asarray(Hitters.iloc[:,list(range(0,14) + list(range(15,18)))])
x1 = sm.add_constant(X)[indices]
x1.shape
model = sm.OLS(y1,x1)
result = model.fit()
print(result.summary())