class Div_by_zero(Exception):
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f'{self.a}'
    def __truediv__(self, other):
            
        try:
           result = self.a / other.a
        except ZeroDivisionError:
            result = 'u cannot div by 0'
        
        return Div_by_zero(result)
    
I1 = Div_by_zero(2)
I2 = Div_by_zero(0)

print(I1/I2)