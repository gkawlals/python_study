# 기호미분
import math as math
import sympy as sym
#Ex_1

x = sym.Symbol('x')
print(sym.diff(sym.sin(x),x)) # cos(x)
print(sym.diff(sym.sin(x),x,x)) # -sin(x)


#Ex_2
def normal_density(x):
    return(sym.exp(-x*x/2)/sym.sqrt(2*math.pi))

print(sym.diff(normal_density(x),x))
# -0.398942280401433*x*exp(-x**2/2)
print(sym.diff(normal_density(x),x ,x))
# 0.398942280401433*(x**2 - 1)*exp(-x**2/2)
print(sym.diff(normal_density(x), x).subs(x,1))
# -0.398942280401433*exp(-1/2)
print(sym.diff(normal_density(x), x).subs(x,1).evalf())
# -0.241970724519143 위에서 나온 값을 정확하게 계산하는 evalf() 함수
print(sym.diff(normal_density(x),x ,x).subs(x,1))
# 0