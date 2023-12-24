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

    def pl(self):
        print("Personal Loan with 11% int")

    def hl(self):
        print("Home Loan with 8% int")


obj1 = FinalAccount()
obj1.savings()
obj1.pl()
obj1.hl()

