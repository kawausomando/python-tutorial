i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# 出力
# 5

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 出力
# [1]
# [1, 2]
# [1, 2, 3]
