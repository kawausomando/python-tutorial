import reprlib
import pprint
import textwrap
import locale

# reprlibはrepr()の別バージョンで、巨大なコンテナお部ジェクトを省略して表示する
charset = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(charset)
# {'a', 'c', 'd', 'e', 'f', 'g', ...}

# pprintはデータ構造を分かりやすく表示してくれる
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

# textwrap.fill()は各段落を指定の幅におさまるように折り返してくれる
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

# localeは国ごとの表現(単位など)を呼び出すことができる
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))
# 1,234,567
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
# $1,234,567.80
