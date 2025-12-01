'''
def st_name(name,id):
    list=f"""
    List
    Name={name}
    ID={id}
    """
    with open("students.txt","w") as f:
        f.write(list)
st_name("Madhu",1)
    with open("students.txt","r") as f:
        f.read()
'''


'''
with open("students.txt","w") as f:
    f.write("Certificate is created for Divya\n")
    f.write("Certificate is created for Kiru")
with open("students.txt","r") as f:
        print(f.read())
'''
#####################################
'''def expense(name,amount):
    list=f"""
    Name={name}
    Amount={amount}
    """
    with open("report.txt","a") as f:
        f.write(list)
expense("Kiru",100)
expense("jii",200)
expense("oiii",300)
with open("report.txt","r") as f:
    print(f.read())'''

###############

'''
def student(name,timestamp):
    if timestamp>6:
        status="Present"
    else:
        status="Not Present"
    list=f"""
    List of students
    Name={name}
    Timestamp={timestamp}
    Status={status}
    """
    with open("attendance.txt","a") as f:
        f.write(list)
student("Preeti",5)
student("Resh",9)
with open("attendance.txt","r") as f:
    print(f.read())
    
'''
###
def supermart(item,quantity,price):
    list=f"""
    Item={item}
    Quantity={quantity}
    Price={price}
    """
    with open("orders.txt","a") as f:
        f.write(list)
supermart("Biscuit",1,9000)
supermart("cofee",2,100)
with open("orders.txt","r") as f:
    print(f.read())


