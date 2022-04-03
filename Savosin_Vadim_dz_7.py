class Complex_num:
    def __init__(self, num):
        try:
            self.complex_num = complex(num)
        except ValueError:
            print(f"{num} нельзя преобразовать в комплексное число")
            self.__init__(input())

    def __str__(self):
        return f'{self.complex_num}'

    def __add__(self, other):
        real = self.complex_num.real + other.complex_num.real
        imag = self.complex_num.imag + other.complex_num.imag
        result = Complex_num(complex(real, imag))
        return result

    def __mul__(self, other):
        real = self.complex_num.real * other.complex_num.real - self.complex_num.imag * other.complex_num.imag
        imag = self.complex_num.imag * other.complex_num.real + self.complex_num.real * other.complex_num.imag
        result = complex(real, imag)
        return result


num1 = Complex_num('2+3j')
num2 = Complex_num(4)
print((num1 + num2))
print((num1 * num2))