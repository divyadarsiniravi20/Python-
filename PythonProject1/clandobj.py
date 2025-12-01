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
car1.display()print()'''

class Employee:
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
e2.display()
