'''try:
    x=int(input("Enter number: "))
    print(10/x)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Division by zero")'''

'''try:
    f=open("data.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing operation completed")'''

'''try:
    value = int("59")
except ValueError:
    print("Invalid Conversion")
else:
    print("Conversion Successful:",value)'''

'''def check_age(age):
    if age < 18:
        raise ValueError("age must be greater than or equal to 18")
    return "Allowed"
print(check_age(13))'''

class LowBudget(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBudget("Insufficient Balance")
    return balance - amount
print(withdraw(10,100))

