# format で {} を利用
print('Happy birth day {} !, You are {} years old now !'.format('Kawauso', '5'))
# Happy birth day Kawauso !, You are 5 years old now !

# 引数の番号指定
print('Happy birth day {0} !, You are {1} years old now !'.format('Kawauso', '5'))
# Happy birth day Kawauso !, You are 5 years old now !

# キーワード引数指定
print('Happy birth day {name} !, You are {year} years old now !'.format(name='Kawauso', year='5'))
# Happy birth day Kawauso !, You are 5 years old now !

# 番号とキーワード引数の混在
print('Happy birth day {0} !, You are {year} years old now !'.format('Kawauso', year='5'))
# Happy birth day Kawauso !, You are 5 years old now !

# float型表記
print('Happy birth day {name} !, You are {year:3f} now !'.format(name='Kawauso', year=5))
# Happy birth day Kawauso !, You are 5.000000 now !

# rを使うとrepr()が適用される
print('Happy birth day Kawauso !, You are {!r} now !'.format(5.12345678))
# Happy birth day Kawauso !, You are 5.12345678 now !

# 小数点以下3桁で表記
import math
print('円周率πはおよそ{0:.3f}である'.format(math.pi))
# 円周率πはおよそ3.142である

# %を使った指定方法
print('円周率πはおよそ%5.3fである' % math.pi)
# 円周率πはおよそ3.142である

# :の後に整数を渡すとフィールドの文字数の最小幅を指定できる
table = {'kawauso': 100, 'mando': 200, 'banjo': 300}
for name, num in table.items():
    print('{0:10} ==> {1:10d}'.format(name, num))

# kawauso    ==>        100
# mando      ==>        200
# banjo      ==>        300

# dictを渡して[]でアクセスすると名前で指定できて便利
print('kawauso: {0[kawauso]:d}; mando: {0[mando]:d}; ' 
    'banjo: {0[banjo]}'.format(table))
# kawauso: 100; mando: 200; banjo: 300

# **表記を使ってキーワード引数として渡しても同じことができる
print('kawauso: {kawauso:d}; mando: {mando:d}; ' 
    'banjo: {banjo}'.format(**table))
# kawauso: 100; mando: 200; banjo: 300

