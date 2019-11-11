vec = [-4, -2, 0, 2, 4]
# 値を2倍にした新しいリストを生成
double = [x*2 for x in vec]

print(double)
# [-8, -4, 0, 4, 8]

# 負の数を除去するフィルター
positive_list = [x for x in vec if x >= 0]
print(positive_list)
# [0, 2, 4]

