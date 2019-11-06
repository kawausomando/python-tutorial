# フィボナッチ級数
# このように多重代入が可能
a, b = 0, 1

while b < 10:
    print(b)
    a, b = b, a+b