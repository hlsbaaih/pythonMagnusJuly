class Sample:

    def M1(self):
        a=10
        b=0
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Zero Division Done")


    def M2(self):
        c=10
        try:
            print(d)
        except NameError as e:
            print(e)
        finally:
            print("Name Error Done")

obj1= Sample()
obj1.M1()
obj1.M2()

