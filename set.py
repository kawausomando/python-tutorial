basket = {'apple', 'orage', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'banana', 'pear', 'apple', 'orage', 'orange'}

print('orange' in basket) # 高速な存在判定
print('crabgrass' in basket)

# 2つの単語からユニークな文字をとって集合演算

a = set('abracadabra')
b = set('alacazam')
# aのユニーク文字
print(a)
# aに存在し、bにはない文字
print(a - b)
# aまたはbに存在する文字
print(a | b)
# aにもbにも存在する文字
print(a & b)
# aまたはbにある共通しない文字
print(a ^ b)

# リスト内包とよく似た集合内包もサポートされている
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)








