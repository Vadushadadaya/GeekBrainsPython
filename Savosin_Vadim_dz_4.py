import random


class Car:
    def __init__(self, s, c, n, police):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = police 
    
    def go(self):
        print('Машина поехала')
        
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('Машина повернула на', random.choice(('право', 'лево')))
    def show_speed(self):
        print('Скорость:', self.speed)        
        
class TownCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, False)
        
    def show_speed(self):
        print('Скорость:', self.speed)  
        if self.speed > 60: 
            print('Превышение скорости')
            
class SportCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, False)
        
class WorkCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, False)
        
    def show_speed(self):
        print('Скорость:', self.speed)  
        if self.speed > 60: 
            print('Превышение скорости')
            
class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n, True)
        
        
        
car_1 = TownCar(70, 'black', 'towncar')
print(car_1.speed, car_1.color, car_1.name, car_1.is_police)
car_1.go()
car_1.stop()
car_1.turn()
car_1.show_speed()
print('\n')

car_2 = SportCar(320, 'orange', 'sportcar')
print(car_2.speed, car_2.color, car_2.name, car_2.is_police)
car_2.go()
car_2.stop()
car_2.turn()
car_2.show_speed()
print('\n')

car_3 = WorkCar(20, 'yellow', 'workcar')
print(car_3.speed, car_3.color, car_3.name, car_3.is_police)
car_3.go()
car_3.stop()
car_3.turn()
car_3.show_speed()
print('\n')

car_4  = PoliceCar(210, 'blue', 'policecar')
print(car_4.speed, car_4.color, car_4.name, car_4.is_police)
car_4.go()
car_4.stop()
car_4.turn()
car_4.show_speed()    
print('\n')