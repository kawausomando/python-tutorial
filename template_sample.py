from string import Template
t = Template('${village}folk send $$10 to $cause.')
sentence = (t.substitute(village='Nottingham', cause='the ditch func'))

print(sentence)
# Nottinghamfolk send $10 to the ditch func.


# substituteメソッドはプレースホルダをディクショナリか
# キーワード引数を渡さないとKeyErrorとなるので、
# safe_substituteメソッドの方が安全な場合がある
# データがなければプレースホルダはそのまま出力される
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
sentence = t.safe_substitute(d)

print(sentence)
# Return the unladen swallow to $owner.