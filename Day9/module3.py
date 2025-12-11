#Build a Student class storing id, name, and marks. Add methods to calculate grade.
'''class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def grade(self):
       if self.marks>90:
           return 'A'
       elif self.marks>80:
           return 'B'
       elif self.marks>70:
           return 'C'
       else:
           return 'D'
s=Student(1,"James",100)
print(s.grade())'''

#Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.
'''class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ElectronicProduct(Product):
    def __init__(self,name,price,years):
        super().__init__(name,price)
        self.years=years
e=ElectronicProduct("Electronic",40000,2)
print(e.name)
print(e.price)
print(e.years)'''

#Create a Payment class with credit-card and UPI subclasses overriding process_payment().
'''class Payment:
    def process_payment(self):
        return "payment class created"
class CreditCard(Payment):
    def process_payment(self):
        return "payment done using credit card"
class UPI(Payment):
    def process_payment(self):
        return "payment done using UPI"
u=CreditCard()
c=UPI()
print(u.process_payment())'''

#Create a Vehicle class and Car, Bike subclasses. Override max_speed().
'''
class Vehicle:
    def max_speed(self):
        return "max speed of vehicle"
class Car(Vehicle):
    def max_speed(self):
        return "max speed of car"
class Bike(Vehicle):
    def max_speed(self):
        return "max speed of bike"
c=Car()
print(c.max_speed())'''

#Implement Operator Overloading: add two objects of BankAccount to return total balance.
'''
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __add__(self,other):
        return self.balance+other.balance
acc1=BankAccount(100)
acc2=BankAccount(200)
total=acc1+acc2
print(total)'''

#Build a ShoppingCart class implementing add, remove, total,apply_discount.
'''
class ShoppingCart:
    def __init__(self):
        self.items={}
    def add(self,item,price):
        self.items[item]=price
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    def total(self):
        return sum(self.items.values())
    def apply_discount(self,percent):
       return self.total()*(1-percent/100)
cart=ShoppingCart()
cart.add('Bag',100)
cart.add('Cart',100)
print(cart.total())'''

#Create a Library class to store books and a method to search by title or author.
'''
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        self.books.append((title,author))
    def search(self,word):
        result=[]
        for title,author in self.books:
            if word.lower() in title.lower() or word.lower() in author.lower():
                result.append((title,author))
                return result
lib=Library()
lib.add_book('Python','John mark')
lib.add_book("Harry Potter","J.K Rowling")
print(lib.search('Python'))'''


