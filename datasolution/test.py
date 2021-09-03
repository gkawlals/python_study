
a = input()
def fit(a):
    c = range(1, a)
    if a == 0:
        print(a)
    elif a == 1 :
        print(a)
    else :
        for i in c:
            a -= a - i
    return a
print(fit(a))


