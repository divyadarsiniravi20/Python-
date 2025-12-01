'''balance=0
class Account:
    def withdraw(self,amount):
        global balance
        balance-=amount
    def deposit(self,amount):
        global balance
        balance+=amount
acc=Account()
acc.withdraw(100)
acc.deposit(70)
print(balance)'''
#a=0
#b=20


''''class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if(a==0):
            return "Error"
        else:
            return a/b
c=Calculator()
print(c.add(10,20))
print(c.div(10,20))
print(c.mul(10,20))
print(c.div(0,20))'''

#####


class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self):
        return self.m1+self.m2+self.m3
    def percentage(self):
        return (self.total()/300)*100
    def display(self):
        print("name: ",self.name)
        print("m1: ",self.m1)
        print("m2: ",self.m2)
        print("m3: ",self.m3)
        print("total: ",self.total())
        print("percent: ",self.percentage())
s=Student("Divya",99,98,90)
s.display()






