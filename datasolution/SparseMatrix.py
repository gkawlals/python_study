import numpy as np
import sparse as sparse
from scipy import sparse
# 희소 행렬 요즘 빅데이터에서 많이 시사화된다.
M = np.reshape(np.zeros(1000*1000), (1000,1000))
M[0,0] = 1
M[999,999] = 1
print(M)
M.nbytes # 8000000 bytes( 1 bytes = 8 bits )

row = np.array([0,999])
col = np.array([0,999])
data = np.array([1,1])

M_csr = sparse.csr_matrix((data,(row, col)))

print(M_csr)
