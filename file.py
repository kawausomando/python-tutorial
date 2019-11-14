# f = open('workfile', 'r+')
# print(f.read())
# 1行目
# 2行目
# 3行目
# 4行目
# f.close()

# print(f.readline())
# print(f.readline())
# 1行目

# 2行目

# print(f.readlines())
# ['1行目\n', '2行目\n', '3行目']

# for line in f:
#     print(line, end='')

# 出力
# 1行目
#
# 2行目
#
# 3行目
    
# print(f.write('4行目'))
# print(f.tell())
# print(f.read())

f = open('workfile', 'rb+')
print(f.write(b'0123456789abscef'))
# 16
print(f.seek(5))
# 5
print(f.read(1))
# b'5'
print(f.seek(-3, 2))
# 16
print(f.read(1))
# b's'
