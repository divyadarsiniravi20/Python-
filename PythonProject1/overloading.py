class Mathops:
    def add(self,a,b,c):
        return a+b+c
m=Mathops()
print(m.add(5,10,20))

class Mathops:
    def add(self,*args):
        return sum(args)
m=Mathops()
print(m.add(5,10,20))