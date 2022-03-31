from abc import abstractmethod

class Clothes:        

    @abstractmethod
    def fabric_cons(self):
        return f"Расход ткани: {(2*self.h + 0.3)}\n"
    
class Coat(Clothes):
    def __init__(self,v):
        self.v=v
    
    @property
    def fabric_cons(self):
        return f"Расход ткани: {(self.v/6.5 + 0.5)}\n"   

class Costume(Clothes):
    def __init__(self,h):
        self.h=h
    
    @property
    def fabric_cons(self):
        return f"Расход ткани: {(2*self.h + 0.3)}\n"


coat = Coat(35)
costume = Costume(180)
print(coat.fabric_cons)
print(costume.fabric_cons)