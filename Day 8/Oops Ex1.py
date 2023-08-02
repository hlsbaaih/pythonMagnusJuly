class Sample:
    a=10
    b=20

    def m1(self):
        print("M1 Functions")

obj1 = Sample() # creating an object for class
print(obj1.a)
obj1.m1()
print(obj1.a+obj1.b)
print(type(obj1)) # to identify the object



