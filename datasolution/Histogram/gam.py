import matplotlib.pyplot as plt
import pandas as pd
from pygam import LinearGAM, l, s

sat = pd.read_csv("/Users/hamjimin/Desktop/DS_Python_ex_vis/sat.csv")


x = sat[["salary", "frac"]]
y = sat[["sat"]]
gam = LinearGAM(l(0) + s(1)).fit(x,y)
gam.summary()

fig, axs = plt.subplots(1,2,figsize=(10,5))
titles = ["salary", "frac"]
for i, ax in enumerate(axs):
    XX = gam.generate_X_grid(term = i)
    pdep, confi = gam.partial_dependence(term=i, width=.95)
    ax.plot(XX[:,i], pdep)
    ax.plot(XX[:,i],confi, c='r',ls='--')
    ax.set_title(titles[i]);


