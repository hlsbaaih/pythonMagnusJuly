class EligibleError(Exception):
    pass

class Sample:

    def eligible(self,age,percentage):
        if age<18 or percentage<60:
            print("Not Eligible For Registration")
        else:
            print("Registration Sucess")
obj1 = Sample()
try:
    obj1.eligible(18,70)
except EligibleError as e:
    print(e)







