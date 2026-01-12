class Employee:
    def __init__(self, name, age, position, emp_id, adress):
        self.name = name
        self.age = age
        self.position = position
        self.emp_id = emp_id
        self.adress = adress

    def display_info(self):
        return f'Name: {self.name}\n  Age: {self.age}\n  Position: {self.position}\n  Employee ID: {self.emp_id}\n  Address :\n{self.adress.display_address()}'
    
    def calculate_salary(self, hrs, rate):
        return hrs * rate


    class Adress:

        def __init__(self, city, state, zip_code,country):
            
            self.city = city
            self.state = state
            self.zip_code = zip_code
            self.country = country

        def display_address(self):
           return f'   City: {self.city}\n   State: {self.state}\n   Zip Code: {self.zip_code}\n   Country: {self.country}'
        

a1 = Employee.Adress("Ahmedabad", "Gujarat", "90001", "India")       
e1 = Employee("khushi", 21, "Intern", "E123", a1)
print(e1.display_info())
print(f'  salary : {e1.calculate_salary(160 , 200)}')
print()


a2 = Employee.Adress("Mumbai" , "Maharashtra", "400001" , "India")
e2 = Employee("Palak" , 22 , "Developer" , "E124" , a2)
print(e2.display_info())
print(f'  salary : {e2.calculate_salary(160 , 300)}')





