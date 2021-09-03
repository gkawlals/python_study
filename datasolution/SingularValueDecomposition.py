import numpy as np
# 특이값 분해
x = np.reshape(np.random.randn(30), (10,3))

U, d, Vt = np.linalg.svd(x, full_matrices=False)
v = np.transpose(Vt)

print(U)
print(d)
print(v)