import numpy as np
A = np.array([[2, -5, 4],
              [1, -2, 1],
              [1, -4, 6]])
                                # <- 역 행렬이 존재하는 경우
B = np.linalg.inv(A)
print(B)

# [[-8. 14.  3.]
#  [-5.  8.  2.]
#  [-2.  3.  1.]]

print(np.linalg.matrix_rank(A)) # 3

A = np.array([[2, -5, 4],
              [1, -2, 1],
              [1, -3, 3]])

                            # <- 역행렬이 존재하지 않는 경우에는 에러가 뜬다.
                            # Singular matrix 
np.linalg.inv(A)
C = np.linalg.matrix_rank(A) # 2
print(C)