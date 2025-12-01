'''with open("app.txt","w") as f:
    f.write("Hello World\n")
    f.write("Python")

with open("app.txt","r") as f:
    content=f.read()
    print(content)'''


#create a file named notes.txt and write 5 lines of text into it.
with open("notes.txt","w") as f:
    f.write("we are learning file\n")
    f.write("With the help of python\n")
    f.write("Today is day 3\n")
    f.write("The previous topic is inheritance\n")
    f.write("It has parent and child classes\n")
with open("notes.txt","r") as f:
    content=f.read()
    print(content)
#Write a program that appends a new line to an existing file notes.txt that says:
"This is an appended line."
with open("notes.txt","a") as f:
    f.write("this is a append line\n")
with open("notes.txt","r") as f:
    print(f.read())
#Write a program that counts the number of lines in a given file.
with open("notes.txt","r") as f:
    count=len(f.readlines())
    print("Length: ",count)
#Write a program that reads a file and counts the number of words in it.
with open("notes.txt","r") as f:
     sentence=f.read()
     words=sentence.split()
     print(len(words))

#Write a program to copy the contents of one file ( source.txt ) to another file ( backup.txt ).

with open("source.txt","w") as f:
    f.write("Copy the text")

with open("source.txt","r") as file:
    text=file.read()

with open("backup.txt","w") as src:
    src.write(text)
with open("backup.txt","r") as dest:
    print(dest.read())
####Write a program that reads a text file and prints only those lines that contain the word "Python"
with open("org.txt","w") as up:
    up.write("Phyton is my fav language\n")
    up.write("I love java")
with open("org.txt","r") as up:
    for l in up:
        if "Phyton" in l:
            print(l)

#Write a program to read a CSV file named students.csv and print name and marks of each student.
with open("students.csv","w") as f:
    f.write("Divya : 100\n")
    f.write("Madhu : 99")
with open("students.csv","r") as f:
    print(f.read())




