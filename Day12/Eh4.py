class Sample:

    def m1(self):
        a=10
        b=0
        try:
            print(a/b)
            print(c)
        except ZeroDivisonError as e:
            print(e)
        except NameError as e1:
            print(e1)


obj1 = Sample()
obj1.m1()
print("End of the program")
