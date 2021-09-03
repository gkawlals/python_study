import numpy as np

# metix n rows and p colmns
A = np.array([[2, -5, 4],
              [1, -2, 1],
              [1, -4, 6]])
type(A)
A.shape
print(A)


# vectors of p elements
x = np.array([-3, 5, 10])
type(x)
x.shape
print(x)

# multiplication of matrices
b = np.matmul(A,x)
print(b)

B = np.transpose(A)
print(B)

c = np.dot(A, A.T) # 여기서 사용하는 .dot과 위의 .matmul()의 함수는 같은 것이다.
print(c)