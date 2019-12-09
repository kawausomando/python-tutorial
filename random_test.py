import random

random.choice(['apple', 'pear', 'banana'])
# リストからランダムにチョイス
# 'apple'

random.sample(range(100), 10)
# range(100)から10個抽出(重複無し)
# [48, 5, 42, 15, 23, 78, 55, 72, 39, 1]

random.random()
# ランダムな浮動小数点数
# 0.2785335302723758

random.randrange(6)
# range(6)からランダムに選んだ整数
# 0