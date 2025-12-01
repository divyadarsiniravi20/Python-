#program that takes two numbers as input and handles division by zero using try–except.

'''num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Division by zero")
'''
from zoneinfo import reset_tzpath

# program to read a file. Handle FileNotFoundError and PermissionError.

'''file=open("open.txt","r")
try:
    print(file.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")'''

#converts a string to integer and handles invalid inputs
'''try:
    value = int("87")
    print(value)
except ValueError:
    print("Incorrect value")
else:
    print("Converted")'''


#safe list access function: if index is out of range, return a message instead of error.

'''try:
    list=["apple","mango","banana"]
    print(list[2])
except IndexError:
    print("Index out of range")
else:
    print("Found")'''

#Write a program to open a CSV file and handle incorrect file format errors.

#raises a custom exception InvalidAgeError if age < 18.

'''def checkage(age):
 if age<18:
    raise InvalidAgeError("Age must be atleast 18")
 return "Allowed"
print(checkage(2))'''

#convert items of a list to integers, handling conversion errors individually.

'''list=[1,2,"kite",3,4,"pineapple"]
new=[]
for i in list:
    try:
     num=int(i)
     new.append(num)
    except ValueError:
     print(f"cannot convert {i} to an integer")
     new.append("null")
print(new)'''

#Create a bank withdrawal function that raises LowBalanceError when balance is insufficient
def withdraw(balance,amt):
    if balance<amt:
      raise LowBalanceError("Balance is insufficient")
    print("sufficient")
print(withdraw(100,200))