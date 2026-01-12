from my_package import mathematical as m


added_res=m.addition(3,6,4,3,9)
print(f"Addition Result is : {added_res}")
print()

m.table(21)
print()

print(m.power(2,10))
print()

print(f'factorial of 5 is:',m.factorial(5))
print()

list_of_numbers = [2,5,8,9]
addition_result = m.addition(*list_of_numbers)
print(f"Addition of {list_of_numbers} is : {addition_result}")
print()

multiplication = m.multiplication(*list_of_numbers)
print(f"Multiplication of {list_of_numbers} is : {multiplication}")
print()