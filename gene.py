sum(i*i for i in range(10)) # 2乗して合計

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec)) # 内積

from math import pi, sin
# sin表
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

# ページの中の重複しない単語
unique_words = set(word for line in page for word in line.split())

# 卒業生総代
valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in rage(len(data)-1, 1, -1))