class Worker:
    def __init__(self, n, s, p, i):
        
        self.name = n
        self.surname = s
        self.position = p
        self._income = i
    
class Position(Worker):
    def __init__(self, n, s, p, i):
        super().__init__(n, s, p, i)
    
    def get_full_name(self):
        print('ФИО:', self.surname, self.name)
        
    def get_total_income(self):
        print('Полный доход:', self._income['wage']+self._income['bonus'])


def info():
    n = input('Введите Имя: ')
    s = input('Введите Фамилию: ')
    p = input('Введите Должность: ')
    w = int(input('Введите Оклад: '))
    b = int(input('Введите Бонус: '))
    i = {'wage':w, 'bonus':b}
    return n, s, p, i


n, s, p, i = info()
W1 = Position(n, s, p, i)
print(f"Имя {W1.name}\n \
Фамилия {W1.surname}\n\
Должность {W1.position}\n\
Доход {W1._income}")
W1.get_full_name()
W1.get_total_income()


n, s, p, i = info()
W2 = Position(n, s, p, i)
print(f"Имя {W2.name}\n\
Фамилия {W2.surname}\n\
Должность {W2.position}\n\
Доход {W2._income}")
W2.get_full_name()
W2.get_total_income()


n, s, p, i = info()
W3 = Position(n, s, p, i)
print(f"Имя {W3.name}\n \
Фамилия {W3.surname}\n\
Должность {W3.position}\n\
Доход {W3._income}")
W3.get_full_name()
W3.get_total_income()
