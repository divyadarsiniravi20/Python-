#import pandas as pd
'''
a=input("Enter the string: ")
v=0
c=0
d=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        v+=1
    elif i not in "aeiou" and i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
print(v)
print(c)
print(d)'''
'''
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''

'''
str=input("Enter string: ")
def word(sentence):
    words=sentence.split()
    freq={}
    for i in words:
        freq[i]=freq.get(i,0)+1
        return freq
print(word(str))
'''

'''
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
   return num1/num2
print(add(num1,num2))
print(sub(num1,num2))
print(mul(num1,num2))
print(div(num1,num2))

'''

'''
list=[10,3,5,6,9]
list.remove(max(list))
print(max(list))'''


'''
num=[2,3,4,5,1,6,7,9,55,8]
add=[n for n in num]
print(add)'''

