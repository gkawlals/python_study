import numpy as np

# solving linear simultaneous equations
A = np.array([[2, -5, 4],
              [1, -2, 1],
              [1, -4, 6]])

b = np.array([-3, 5, 10])

x = np.linalg.solve(A, b)
print(x)                    # [124.  75.  31.]
# singular matrix인 경우에는 에러가 뜬다.