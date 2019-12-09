def average(values):
    """数値のリストから算術平均を計算
    
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()
# 埋め込まれたテストを自動で検証する

