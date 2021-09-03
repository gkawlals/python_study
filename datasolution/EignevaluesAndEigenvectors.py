# 고유값과 고유 백터
import numpy as np

C = np.array([[1.0, 0.4, 0,2],
              [0.4, 1.0, 0.4],
              [0.2, 0.4, 1.0]])

values, Vectors = np.linalg.eig(C)

print(values) # 고유값

print(Vectors) # 고유백터