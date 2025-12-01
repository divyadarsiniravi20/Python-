#second largest number
'''num=[23,89,12,78,55,42]
l=0
s=0
for n in num:
    if n>l:
        s=l#0=0
        l=n
    elif l>n>s:
        s=n
print(s)

#Move all zero to end
num2=[0,3,0,5,7,0,9]
num1=[]
zero=0
for n in num2:
    if n==0:
        zero+=1
    else:
        num1.append(n)
result=num1+[0] *zero
print(result)

#Interchange first and last element
alpha=['a','b','c','d','e']
for n in alpha:
 alpha[0],alpha[-1]=alpha[-1],alpha[0]
print(alpha)

#only prime numbersprime
prime=[10,11,12,13,17,20,23]
for n in prime:
    if n<2:
        continue
    for i in range(2,int(n**0.5)):
        if n%i==0:
            break
    else:
            print(n)'''
#indices of the given value
 #nums=[5,2,7,5,9,5,3]
#n=int(input("Enter a number: "))
#print(nums.index(n))


#LIST-EXERCISE(5i) negative first positive next
'''nums=[2,-1,4,-9,-4,6]
neg=[]
pos=[]
for n in nums:
    if n<0:
        neg.append(n)
for i in nums:
    if i>0:
        pos.append(i)
res=neg+pos
print(res)'''
#Exercise2 elements more than once

'''e=[1,2,3,2,4,1,5,1]
c=[]
for i in e:
    if e.count(i)>1 and i not in c:
        c.append(i)
print(c)'''

#Exercise3 rotate a list to left


#exercise4 remove string length less than 3
'''a=["bat","ball","ap","orange"]
ap=[]
for i in range(len(a)):
    if(len(a[i])>3):
        ap.append(a[i])
print(ap)'''

#exercise5
a=[[1, 2], [3, 4], [5]]
new=[]
for i in a:
    for j in i:
        new.append(j)
print(new)#''''''










