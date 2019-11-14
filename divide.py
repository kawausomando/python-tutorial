def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("ゼロ除算エラー")
    else:
        print('答え: ', result)
    finally:
        print('in finally')

divide(2, 1)
# 答え:  2.0
# in finally

divide(2, 0)
# ゼロ除算エラー
# in finally

divide("2", "1")
# in finally
# Traceback (most recent call last):
#   File ".\divide.py", line 15, in <module>
#     divide("2", "1")
#   File ".\divide.py", line 3, in divide
#     result = x / y
# TypeError: unsupported operand type(s) for /: 'str' and 'str'