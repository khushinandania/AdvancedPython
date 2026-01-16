import os

try:
   with open('data.txt' , 'r') as f:
       content = f.read()
       print("data read from text file.")
       print(content)
except FileNotFoundError:
    print("ERROR:file not found.")

print()




with open('data1.txt' , 'w') as f:
    f.write("This is a sample text file.\n It contains multiple lines of text.\n")

try:
   with open('data1.txt' , 'r') as f:
       content = f.read()
       print("data read from text file.")
       print(content)
except FileNotFoundError:
    print("ERROR:file not found.")

print()


                                                                                                                                                                                                                                                                                         

with open('data2.txt' , 'a') as f:
    f.write("this is simple text file that contains basic file handling theory in python.\n")

os.chmod('data2.txt' , 0o444)  #read-only permission

try:
    with open('data2.txt' , 'a') as f:
        f.write("Trying to append more data.\n")
except FileNotFoundError:
    print("ERROR:file not found.")
except PermissionError:
    print("ERROR:Permission denied. Cannot write to read-only file.")





