class MyClass:
    def __init__(self):
        pass
    def f(self, word):
        print(word)
        
x = MyClass()

# データ属性の追加・参照
x.counter = 1 # データ属性は事前に宣言する必要はない
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter) # 16
del x.counter

# メソッドの参照
x.f("hello kawauso")

xf = x.f
xf('hello kawauso again') # 出力: hello kawauso again
