# 수치 미분

# Ex_1 : f(x) = sin(x)  => f'(x) = ? at x = 0.5
import numpy as np
import math as math
def derivative(f, a, h=1e-4):
    return (f(a+h) - f(a - h)) /(2*h)

print(derivative(np.sin, a=0.5, h=1e-4) )# 근사값 : 0.8775825604276366
print(np.cos(0.5))                         # 정확값 : 0.8775825618903728

# Ex_2 f(x) = 1/2^pi exp(-1/2x^2 => f'(x) = ? at x = 1

def normal(z):
    return(np.exp(-z*z/2) / np.sqrt(2*math.pi))
print(derivative(normal, a=1, h=1e-4)) # 근사값 : -0.2419707237125146

def normal_prime(z):
    return(-z*np.exp(-z*z/2) / np.sqrt(2*math.pi))
print(normal_prime(z=1)) # 정확값 : -0.24197072451914337

# 2계미분
# Ex_1
def derivaltive_2(f,a,h=1e-4):
    return (derivative(f,a+h, h) - derivative(f,a-h,h)) / (2*h)

print(derivaltive_2(np.sin, a=0.5, h=1e-4)) # 근사값 : -0.4794255381579404
print(-np.sin(0.5))                         # 정확값 : -0.479425538604203

# Ex_2
print(derivaltive_2(normal, a=1, h=1e-4)) # 정확값 : 0.0
