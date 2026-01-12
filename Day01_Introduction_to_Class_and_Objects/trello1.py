class Car:

    def __init__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #instance method
    def display_info(self):
        return f'car make: {self.make}\n model:{self.model}\n model year: {self.year}'
    
    

c1 = Car("Audi","A4",2017)
c2  = Car("BMW","X3",2014)

print(c1.display_info())
print("-----")
print(c2.display_info())

