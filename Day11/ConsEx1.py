class Sample:

    def m1(self):
        print("M1 Function")

    def m2(self):
        print("M2 Function")

    def __init__(self,a,b):
        print(a+b)


obj1 = Sample(10,30)
obj1.m1()
obj1.m2()
