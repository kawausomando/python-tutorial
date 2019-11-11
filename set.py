basket = {'apple', 'orage', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'banana', 'pear', 'apple', 'orage', 'orange'}

print('orange' in basket) # 高速な存在判定
# True
print('crabgrass' in basket)
# False

# 2つの単語からユニークな文字をとって集合演算
a = set('abracadabra')
b = set('alacazam')

# aのユニーク文字
print(a)
# {'r', 'a', 'c', 'b', 'd'}

# aに存在し、bにはない文字
print(a - b)
{'r', 'b', 'd'}

# aまたはbに存在する文字
print(a | b)
# {'z', 'r', 'a', 'c', 'b', 'd', 'l', 'm'}

# aにもbにも存在する文字
print(a & b)
# {'c', 'a'}

# aまたはbにある共通しない文字
print(a ^ b)
# {'m', 'b', 'l', 'z', 'd', 'r'}

# リスト内包とよく似た集合内包もサポートされている
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}