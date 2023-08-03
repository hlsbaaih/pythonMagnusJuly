class Grandparent:
    def a1(self):
        print("3 assets")
class parent(Grandparent):
    def a2(self):
        print("2 asset")
class son(parent): # a1,a2,and a3
    def a3(self):
        print("1 asset")

obj1 = son()
obj1.a1()
obj1.a2()
obj1.a3()
