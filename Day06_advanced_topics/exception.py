name = input("enter your name:")


class InvalidMarksError(Exception):
    pass 

try :
    maths = int(input("enter maths marks:"))
    phy = int(input("enter physics marks:"))
    eng = int(input("enter english marks:"))

    marks = [maths , phy , eng]

    for i in marks:
        if i<0 or i>100:
            raise InvalidMarksError("marks must be between 0 to 100")
    
    avg_marks  = sum(marks)/len(marks)

    print(f"{name} your average score is :" , avg_marks)

except ValueError:
    print("error : please enter valid integers")

except InvalidMarksError as e:
    print("custom error:" , e)

else :
    if (avg_marks>75):
        print("you scored really well")
    elif(avg_marks<75 and avg_marks > 35):
        print("you need to work hard")
    else:
        print("you failed!")

finally:
    print("program execution is done.")