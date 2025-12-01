class Animal:
    def speak(self):
        print("Animal make sound")
class Dog(Animal):
    def bark(self):
        print("Dog bark")
d=Dog()#obj is created for child class
d.speak()
d.bark()

####super

class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,id):
        super().__init__(name)
        self.id=id
e=Employee("Swetha",1)
print(e.name,e.id)



