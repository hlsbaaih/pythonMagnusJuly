from abc import ABC, abstractmethod

class Accounts:

     def savings(self):
         print("No Min Balance and Earn upto 7.5% monthly Int")

class Loans(ABC):


    @abstractmethod
    def pl(self):
        print("Personal Loan")

    @abstractmethod
    def hl(self):
        print("House Loan")

class FinalAccount(Accounts,Loans):
    pass

obj1 = FinalAccount()
obj1.savings()
obj1.pl()
obj1.hl()

