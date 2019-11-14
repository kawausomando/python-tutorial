class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
# 出力
# My exception occurred, value: 4

raise MyError('oops!')
# 出力
# Traceback (most recent call last):
#   File ".\exception_class.py", line 12, in <module>
#     raise MyError('oops!')
# __main__.MyError: 'oops!'