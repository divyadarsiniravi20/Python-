'''data={1,2,3,4}
print(data)

empty=set()
print(empty)
s={5,6,7,8}
s.remove(5) # removes element but shows error if not found
print(s)
s.add(100)
print(s)
s.discard(5000)# remove element but no error if not found
print(s)'''

'''a={1,2,3}
b={3,4,5}
print(a|b)#union 
print(a&b)#intersection
print(a-b)#unique in a
print(b-a)#in b unique
print(a^b)#unique both'''

'''s={10,20,30}
print(20 in s)

for items in {2,4,6}:
    print(items)

l=[1,2,2,3,4,5]
unique=list(set(l)) # conversion of list to set and then getting the list
print(unique)'''

student ={
    "name":"Divya",
    "age":22,
    "City":"Coimbatore"
}
'''print(student["name"])
print(student["age"]) #OR
print(student.get("name"))
student["email"]="divya@gmail.com"
student["city"]="Abu Dhabi"
#print(student)
#student.pop("age")
#del student["age"]
student.clear()
print(student)
#student.clear()'''
for k in student.keys():
    print(k) #left
for v in student.values():
    print(v) #right
for k,v in student.items():
    print(k,v) #all