class base():
    def a(self):
        print('私はbase.aです.base.bをコールします')
        self.b()
    def b(self):
        print('私はbase.bです.der.bでオーバーライドされます')

class der(base):
    def b(self):
        print('私はder.bです.')


b = base()
d = der()

b.a()
# 私はbase.aです.base.bをコールします
# 私はbase.bです.der.bでオーバーライドされます

d.a()
# 私はbase.aです.base.bをコールします
# 私はder.bです.