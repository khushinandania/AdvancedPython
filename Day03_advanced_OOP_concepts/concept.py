class Vehicle:

    def __init__(self ,brand, speed):
        self.brand=brand
        self.speed=speed
    
    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")

    def fuel_type(self,fuel):
        self.fuel = fuel
        print(f"Fuel type: {self.fuel}")

class Car(Vehicle):  #inheritance

    def fuel_type(self,fuel): #overriding
        self.fuel = fuel
        print("car can use petrol or diesel or CNG")
        print(f"this car uses {self.fuel}")


class Bike(Vehicle):  #inheritance

    def fuel_type(self,fuel):  #overriding
        self.fuel = fuel
        print("bike can use petrol or run on electricity")
        print(f"this bike uses {self.fuel}")


truck = Vehicle("eicher" ,70)

c1 = Car("swift" , 100)
c2 = Car("honda city" , 120) 

b1 = Bike("pulsar" , 80)
b2 = Bike("tvs" , 60)

truck.show_info()
truck.fuel_type("diesel")

print("------")
c1.show_info()
c1.fuel_type("petrol")

print("------")
c2.show_info()
c2.fuel_type("CNG")

print("------")

b1.show_info()
b1.fuel_type("petrol")

print("------")
b2.show_info()
b2.fuel_type("electricity")
print()
print("---------------------------")
print()




from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self , name , emp_id,age):
        self.name = name
        self.emp_id = emp_id
        self.age = age

    @property  #getter
    def age(self):
        return self._age
    
    @age.setter  #setter
    def age(self,age):
        if age < 18:
            print("Age must be at least 18")
        else:
            self._age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")    
        print(f"Age: {self._age}")

    
    @abstractmethod    #abstract method
    def calculate_salary(self,hrs ,rate):
        pass

class FullTimeEmployee(Employee):

    def calculate_salary(self,hrs,rate):
        salary = hrs * rate
        return salary 

class PartTimeEmployee(Employee):

    def calculate_salary(self,hrs,rate):
        salary= hrs * rate * 0.3
        return salary


e1 = FullTimeEmployee("John",101,25)


e1.show_info()
print(f"full time salary : {e1.calculate_salary(168 ,250)}")

print("------")
e2 = PartTimeEmployee("Jane",102,25)
e2.show_info()
print(f"part time salary : {e2.calculate_salary(84 ,250)}")