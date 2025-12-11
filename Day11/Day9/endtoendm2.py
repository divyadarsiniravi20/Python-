#Given a list of product prices, remove duplicates while maintaining order.
'''list=[22,76,82,22,50,120]
newlist=[]
c=0
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist);'''
#Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.
'''
list1=[2,33,12]
list2=[20,33,1]
l=dict(zip(list1,list2))
print(l)'''
#Given a dictionary of student marks, return the top 3 students.
'''from collections import Counter
m={"a":90,"b":98,"c":67,"d":100}
s=Counter(m).most_common(3)
print(s)'''
#Flatten a nested list like [[1,2],[3,4],[5,6]] into a single list.
'''
list=[[1,2],[3,4],[5,6]]
new=[x for n in list for x in n]
print(new)'''
#Find common elements between three sets.
'''
set1={1,2,3}
set2={3,5,6}
set3={3,5,6}
print(set1 & set2 & set3)'''
#Convert a list of tuples to a dictionary only if keys are unique.
'''tuple=[("a",1),("b",2),("c",3),("a",4)]
d={}
for n,i in tuple:
    if n not in d:
        d[n]=1
print(d)'''
#print(dict(tuple))
#Given a tuple of names, return one tuple with unique names.
'''
name=("Divya","Rupa","Divya","Anu")
unique=tuple(dict.fromkeys(name))
print(unique)
'''
#From a dictionary of employees, filter only employees with salary above 60000.
'''
employees={
    "Alice":55000,
"Bob":55000,
"Charlie":55000,
"David":65000
}
value={k:v for k,v in employees.items() if v>60000}
print(value)
'''
#Given two dictionaries, combine them but sum values for matching keys.
d1={"a":10,"b":20,"c":30}
d2={"b":10,"c":20,"d":20}
result={}
for k in set(d1)|set(d2):
    result[k]=d1.get(k,0)+d2.get(k,0)
print(result)

