from timeit import Timer

time1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
time2 = Timer('a,b = b,a', 'a=1; b=2').timeit()

print(time1)
# 0.020502762
print(time2)
# 0.018866841999999995