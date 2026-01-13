with open('file.txt' , 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is simple text file .it introduces about file handling in python\n")


with open('file.txt' , 'r') as f:
    content = f.read()
    print(content)


with open('file.txt' , 'a') as f:
    f.write("there is some functions to handle files in python like read , write , append etc.\n")
    f.writelines(["files can be handled using 'with' statement as well as without 'with' statement.\n" , "recommended way to use file handling is by using 'with' statement.\n"])

with open('file.txt' , 'r') as f:
    content = f.read()
    print(content)


f = open('file2.txt' , 'w')
f.write("this is another file created using open function without 'with' statement.\n")
f.close()


with open('file2.txt' , 'a+') as f:
    f.write("this line is added in read and write mode.\n")
    f.seek(0)  # move the cursor to the beginning of the file
    content = f.read()
    print(content)

