
#take three numbers as input and print the largest.
'''a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)'''


#string pallindrome
'''str="viv" #input("Enter a string: ")
a=len(str)
rev=""
for i in range(a-1,-1,-1):
   rev=rev+str[i]
if(rev == str):
    print("yes")
else:
    print("no")'''

#program to count how many times each character appears in a string.

'''str="apple"
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)'''

#to remove all special characters from a string.
'''str="D_i_vya"
for i in str:
    if i.isalpha():
        print(i,end="")
'''

'''list=[1,2,3,4,4,5,6]
b=len(list)
new=[]
for i in list:
   if i not in new:
        new.append(i)
print(new)

list=[1,2,3,3,4,5]
nw=[]
for i in list:
    if i not in nw:
        nw.append(i)
print(nw)'''

##list to the right by N positions.

'''def rotate_right(lst,n):
    n=n%len(lst)
    return lst[-n:]+lst[:-n]
num=[1,2,3,4,5]
print(rotate_right(num,3))'''

#Given a list of strings, return a new list containing only strings longer than 4 characters.
'''list=["Apple","hat","mug","people"]
new=[]
for i in list:
    if len(i) >4:
        new.append(i)
print(new)'''

#Write a program to convert a list of tuples into a dictionary.

'''t=(("name","Divya"),("age",22),("Salary",9800000))
my=dict(t)
print(my)'''

#find the second largest number.
t=(110,10,11,43)
p=()
for i in t:
  p.append(sorted(i))
  print(p)















