class Father:
    def home(self):
        print ("2 Flats 2 Plots with house")
class Mother:
    def car(self):
        print("2 cars")
    def cash(self):
        print("1 billion cash")
class son(Father,Mother):
    pass

obj1 = son()
obj1.home()
obj1.car()
obj1.cash()



