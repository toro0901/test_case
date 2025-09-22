class Calculator:
    def add(self,x,y):
        result = x + y
        return result
    
    def double_x(self,x):
        result = x * 2
        return result
    
calculator = Calculator()
x = 3
y = 5

print(calculator.add(x=x, y=y))
print(calculator.double_x(x=x))