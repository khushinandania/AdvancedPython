class Car:

    manufacture_country = "Germany"  #class variable


    #constructor
    def __init__(self , make, model, year,speed):
        self.make = make
        self.model = model
        self.year = year
        self._speed = speed

    def get_speed(self):  #Accessor method
        return self._speed
    
    def set_speed(self, speed): #Mutator method
        if speed >= 0:
            self._speed = speed
        else:
            self._speed = 0
            print("Speed cannot be negative. Setting speed to 0.")


    #instance method
    def display_info(self):
        
        return f'car make: {self.make}\n model:{self.model}\n year: {self.year}'
    
    def calculate_age(self , curr_year):
        return curr_year-self.year
    
    #class method
    @classmethod
    def get_manufacture_country(cls):
        return cls.manufacture_country
    
    #static method
    @staticmethod
    def is_classic(year):
        return year < 1990
    

c1 = Car("Audi","A4",2017,250)
c2  = Car("BMW","X3",2014,230)

print(c1.display_info())
print("Age of car Audi:", c1.calculate_age(2026))
c1.set_speed(150)
print("Speed :", c1.get_speed())
print(f'is {c1.make} {c1.model} which is made in {c1.year} is classic car ? :' , Car.is_classic(c1.year))
print("-----")


print(c2.display_info())
print("Age of car BMW:", c2.calculate_age(2026))
print(f'speed:' ,c2.get_speed())
print()

print("all cars are manufactured in :" , Car.get_manufacture_country())
print()
print("is 1985 classic car? :" , Car.is_classic(1985))
print()

