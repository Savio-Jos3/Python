class A:
    def methodA(self):
        print("Method of Class A")

class B(A):
    def methodB(self):
        print("Method of Class B")

class C:
    def methodC(self):
        print("Method of Class C")

class D(B, C):  # Hybrid: Multilevel + Multiple
    def methodD(self):
        print("Method of Class D")

d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
