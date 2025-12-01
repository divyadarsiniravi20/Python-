
#Exercise 6
#Create a class Product with attributes name, price, quantity. Add a method to calculate the total cost of all quantities.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total(self):
        print(self.price * self.quantity)

p=Product("Divya",100,5)
p.total()


#Create a class Customer with attributes name, age, city. Add a method that checks if the customer is eligible for a loyalty program (age > 25).

class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def check(self):
        if self.age>25:
            print("Eligible")
        else:
            print("Not Eligible")
c=Customer("Ramesh",38,"Cochin")
c.check()

#Create a class BankAccount that supports deposit, withdraw, check balance, and displays transaction logs.

balance=100
class BankAccount:
    def __init__(self,name,deposit,withdraw):
        self.name=name
        self.deposit=deposit
        self.withdraw=withdraw
        self.balance=balance
    def dep(self):
        print(self.deposit+self.balance)
    def wit(self):
        print(self.balance-self.withdraw)
b=BankAccount("ramesh",1000,500)
b.dep()
b.wit()

#Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage.storage
storage=128
class Mobile:
    def __init__(self,brand,model,store):
        self.brand=brand
        self.model=model
        self.store=store
    def upgrade(self):
        if(self.store > storage):
            print(self.store)
m=Mobile("samsung","S24",256)
m.upgrade()

#Create a class Student with three subject marks. Add methods for total, percentage, and grade (A, B, C, D).
class Student:
     def __init__(self,m1,m2,m3):
            self.m1=m1
            self.m2=m2
            self.m3=m3
     def total(self):
         print(self.m1+self.m2+self.m3)
     def percent(self):
         print(self.total/300)*100
     def grade(self):
         if(self.m1>90 or self.m2>90 or self.m3>90):
             print("A")
         elif(self.m1>80 or self.m2>80 or self.m3>80):
             print("B")
         elif(self.m1>70 or self.m2>70 or self.m3>70):
             print("C")
         else:
             print("D")
s=Student(88,89,71)
s.grade()
#######################################################
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_item(self,name,price):
        self.items.append((name,price))
        print(name,"added to cart")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print(name,"removed from cart")
                return
        print(name,"not in cart")
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
            return total
    def apply_discount(self,percent):
        total=self.total_cost()
        discount_amount=total*(percent/100)
        final_price=total-discount_amount
        return final_price
    def display_items(self):
        if not self.items:
            print("Empty cart")
            return
        print("items in cart:")
        for name,price in self.items:
            print(name,"-",price)
cart=ShoppingCart()
cart.add_item("samsung",100)
cart.add_item("apple",500)
cart.add_item("mango",200)
print()
cart.display_items()
print()
print("tc:",cart.total_cost())
print("final price:",cart.apply_discount(10))
print()
cart.remove_item("mango")
cart.display_items()











