from tkinter.font import names
class Company():
    def __init__(self,cname):
        self.cname=cname

class Employee(Company):
    def __init__(self,cname,name,id):
        super().__init__(cname)
        self.name=name
        self.id=id
e=Employee("EY","Divya",1)
print(e.cname,e.name,e.id)

#####
class BankAccount:
    def __init__(self,bankname):
        self.bankname=bankname
class SavingsAccount(BankAccount):
    def __init__(self,bankname,custname,salary):
        super().__init__(bankname)
        self.custname=custname
        self.salary=salary
s=SavingsAccount("SBI","Divya",9800000)
print(s.bankname)
print(s.custname)
print(s.salary)

######MULTILEVEL INHERITANCE

class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,empid):
        super().__init__(name)
        self.empid=empid
class Manager(Employee):
    def __init__(self,name,empid,salary):
        super().__init__(name,empid)
        #super().__init__(empid)
        self.salary=salary
m=Manager("Divya",1,100000000)
print(m.name,m.empid,m.salary)

class Device:
    def __init__(self,type):
        self.type=type
class Computer(Device):
    def __init__(self,type,price):
        super().__init__(type)
        self.price=price
class Laptop(Computer):
    def __init__(self,type,price,warrenty):
        super().__init__(type,price)
        self.warrenty=warrenty
l=Laptop("Lap",30000,2)
print(l.type,l.price,l.warrenty)

#######Multiple Inheritance

class Camera:
    def __init__(self,pixel):
        self.pixel=pixel
class Phone:
    def __init__(self,model):
        self.model=model
class Smartphone(Camera,Phone):
    def __init__(self,pixel,model,price):
        Camera.__init__(self,pixel)
        Phone.__init__(self,model)
        self.price=price
s=Smartphone(1080,"s24",50000)
print(s.model,s.price)

class ElectricVehicle():
    def __init__(self,vnum):
        self.vnum=vnum
class FuelVehicle():
    def __init__(self,fuelcost):
        self.fuelcost=fuelcost
class HybridCar(ElectricVehicle,FuelVehicle):
    def __init__(self,vnum,fuelcost,price):
        ElectricVehicle.__init__(self,vnum)
        FuelVehicle.__init__(self,fuelcost)
        self.price=price
h=HybridCar(1001,3000,450000000)
print(h.vnum,h.fuelcost,h.price)


#####Hierarchical Inheritance
class Vehicle:
    def __init__(self,vnum):
        self.vnum=vnum
class Car(Vehicle):
    def __init__(self,vnum,cprice):
        Vehicle.__init__(self,vnum)
        self.cprice=cprice
class Bike(Vehicle):
    def __init__(self,vnum,milage):
        Vehicle.__init__(self,vnum)
        self.milage=milage
class Truck(Vehicle):
    def __init__(self,vnum,trucknum):
        Vehicle.__init__(self,vnum)
        self.trucknum=trucknum
c=Car(2034,100000)
b=Bike(2000,10)
t=Truck(2005,123)
print(c.vnum,c.cprice)

class Shape:
    def __init__(self,appearance):
        self.appearance=appearance
class Circle(Shape):
    def __init__(self,appearance,radius):
        Shape.__init__(self,appearance)
        self.radius=radius
class Rectangle(Shape):
    def __init__(self,appearance,l):
        Shape.__init__(self,appearance)
        self.l=l
class Triangle(Shape):
    def __init__(self,appearance,side):
        Shape.__init__(self,appearance)
        self.side=side
c=Circle("Shapes",55)
r=Rectangle("Rect",10)
t=Triangle("Trio",3)
print(c.appearance,c.radius)