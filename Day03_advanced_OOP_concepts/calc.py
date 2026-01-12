class Calculator:

    
    @staticmethod
    def addition(a ,b):
        return a+b
    
    def subtraction(self ,a ,b):
        return a-b
    
    def multiplication(self ,a ,b):
        return a*b
    
    def division(self , a,b):
        if b != 0:
            return a/b
        else:
            return "Error! Division by zero."
        

calc = Calculator()

print(f"Addition: {Calculator.addition(10, 5)}")
print(f"Subtraction: {calc.subtraction(10, 5)}")
print(f"Multiplication: {calc.multiplication(10, 5)}")
print(f"Division: {calc.division(10, 0)}")