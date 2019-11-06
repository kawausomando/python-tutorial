# リスト全体のスライスコピーにループをかける
words = ['cat', 'window', 'defenstrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

# 出力
# ['defenstrate', 'cat', 'window', 'defenstrate']