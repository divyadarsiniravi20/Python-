'''class Student:
    pass#just executing
s1=Student()
s2=Student()'''
####################
'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student(name="Divya",age=20)
print(s1.name)'''
#####################3
'''class Car:

    def __init__(self,brand,model,price):#constructor
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):#method
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)

car1=Car("Hyundai","Swift","7600000")

car1.display()
print()'''
######################
'''class Employee:
      def __init__(self,name,empid):
          self.name=name
          self.empid=empid
      def display(self):
          print("Name: ",self.name)
          print("Id: ",self.empid)

e1=Employee("Harsh","123456")
e1.display()
print()
e2=Employee("Divya","123456")
e2.display()'''
#####################################
'''balance=0
class BankAccount:
    def withdraw(self, amount):
        global balance
        balance -= amount
    def deposit(self,amount):
        global balance
        balance+=amount
b1=BankAccount()
b1.deposit(100)
b1.withdraw(10)
print(balance)'''
##
balance=0
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
print(balance)







