# __next__()メソッドの付いたオブジェクトを返す__iter__()メソッドを定義する
# すでに__next()__が定義してあるクラスでは__iter__()はselfを返すだけでよい
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)

# m
# a
# p
# s