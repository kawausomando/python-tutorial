import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10) # 参照を生成する
d = weakref.WeakValueDictionary()
d['primary'] = a # 参照を生成しない
print(d['primary']) # オブジェクトが生きていれば取ってくる
10

del a # 参照を削除
gc.collect() # ガベージコレクションを実行

d['primary'] # エントリは自動的に削除されている
# Traceback (most recent call last):
#   File ".\weakref_sample.py", line 17, in <module>
#     d['primary'] # エントリは自動的に削除されている
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.1520.0_x64__qbz5n2kfra8p0\lib\weakref.py", line 137, in __getitem__      
#     o = self.data[key]()
# KeyError: 'primary'