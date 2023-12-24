from abc import ABC, abstractmethod

class Accounts:

     def savings(self):
         print("No Min Balance and Earn upto 7.5% monthly Int")

class Loans(ABC):

]
    @abstractmethod
    def pl(self):
        print("Personal Loan")

    @abstractmethod
    def hl(self):
        print("House Loan")


obj1 = Accounts()
obj2 = Loans()
obj1.savings()
obj2.pl()
obj2.hl()

