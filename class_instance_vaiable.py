class Dog:
    
    kind = '柴' # クラス変数
    
    def __init__(self, name):
        self.name = name # インスタンス変数
        
        
taro = Dog('太郎')
jiro = Dog('次郎')

# クラス変数の参照
print(taro.kind) # 柴
print(jiro.kind) # 柴

# インスタンス変数の参照
print(taro.name) # 太郎
print(jiro.name) # 次郎