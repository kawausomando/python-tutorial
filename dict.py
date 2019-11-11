# 初期化
tel = {'jack': 4098, 'sape': 4139}
# 追加
tel['guido'] = 4127
print(tel) # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack']) # 4098

# 削除
del tel['sape']
tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

# キーのリストを取得
print(list(tel.keys()))
# ['jack', 'guido', 'irv']

# キーでソート
print(sorted(tel.keys()))
# ['guido', 'irv', 'jack']

# 存在チェック
print('guido' in tel) # True
print('jack' not in tel) # False

# dict()コンストラクタは、キー:値ペアのタプルからなるシーケンスから
# ディクショナリを構築する
tel2 = dict([('sape', 4139), ('guide', 4127), ('jack', 4098)])
print(tel2)
# {'sape': 4139, 'guide': 4127, 'jack': 4098}

# 辞書内包を使えばキーと値を与える任意の式からディクショナリが生成できる
print({x: x**2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# キーが文字列なら、キーワード引数でペアを指定するのが楽な場合もある
tel3 = dict(sape=4139, guido=4127, jack=4098)
print(tel3)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
