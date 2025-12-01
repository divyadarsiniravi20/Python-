'''numbers=[10,20,30,40,50]
fruits=["Divya","Rithu","Anisha","Mubenna"]
mixed=[10,"kite",98,"lollipop","flower",55]
print(numbers[0])
print(numbers[-1])
print(numbers)
mixed.pop(0)
print(mixed)
del numbers[0]
print(numbers)
numbers.append(99)
print(numbers)'''

#25/11/2025
numbers=[10,20,30,40,50]
print(numbers[1:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[:3])
#print(numbers[0::])
print(max(numbers))
print(min(numbers))
print(len(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

num=[1,2,3,4]
squares= [n*n for n in num] #list comprehension
print (squares)


