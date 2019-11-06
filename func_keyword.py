def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ');

# 次のいずれの形でもコールできる
parrot(1000)                                         # 位置引数1個
parrot(voltage=1000)                                 # キーワード引数1個
parrot(voltage=100000000, action='VOOOOOM')          # キーワード引数2個
parrot(action='VOOOOOOOM', voltage=1000000)          # キーワード引数2個
parrot('a million', 'bereft of life', 'jump')        # 位置引数3個
parrot('a tousand', state='pushing up the daisies')  # 位置引数1個キーワード引数1個

# 次のコールは無効
# parrot()                     # 必要な引数がない
# parrot(voltage=5.0, 'dead')  # キーワード引数の後に非キーワード引数
# parrot(110, voltage=220)     # 同じ引数に値を2度与えた
# parrot(actor='John Cleese')  # 未知のキーワード引数