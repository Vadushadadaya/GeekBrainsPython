class Stationery:
    def __init__(self):
        self.title =  "Hello, World!"
    
    def draw(self):
        print('Запуск отрисовки')
        
class Pen(Stationery):   
    def draw(self):
        print("\033[3m\033[34m\033[47m{}\033[0m".format(self.title))

class Pencil(Stationery):
    def draw(self):
        print("\033[1m\033[30m\033[47m{}\033[0m".format(self.title))    
    
class Handle(Stationery):
    def draw(self):
        print("\033[1m\033[32m\033[47m{}\033[0m".format(self.title))    

pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()

pen_1.draw()
pencil_1.draw()
handle_1.draw()