'''square = lambda x:x*x
print(square(5))

add=lambda a,b:a+b
print(add(3,4))'''

'''generate_line=lambda user:f"Hello{user},welcome to python training"
def write_dynamic_line(user,filename):
    with open(filename,"w") as f:
        f.write(generate_line(user))
write_dynamic_line("Rahul","welcome.txt")'''

def write_dynamic_record(emp_id,name,salary):
    record=f"""
    Employee Record
    ID: {emp_id}
    Name: {name}
    Salary: {salary}
    """
    with open("employee.txt","w") as f:
        f.write(record)
write_dynamic_record(101,"Aman",75000)