class Road():
    def __init__(self, l, w):
        self._length = l
        self._width = w
    
    def weight(self):
        W = self._length*self._width*25*5*0.001
        print(W,'т')
        
        
R = Road(5000, 20)
R.weight()