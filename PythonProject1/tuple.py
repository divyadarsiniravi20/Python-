'''fruits=["apple","banana","mango"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

nums=[1,2,3,4,5]
print(nums.count(5))
print(nums.index(5))
letters=["a","b","c","d","e","f","g"]
print(letters.index("g"))'''

'''data=10,20,30 #packing and unpacking
a,b,c=data
print(a,b,c)
employee=("John",32,("Banglore","India"))
print(employee[0][2])'''

n=[33,20,45,66]
maxi=n[0]
mini=n[0]
for i in n:
    if i>maxi:
        maxi=i
    elif i<mini:
        mini=i
print(maxi,mini)

