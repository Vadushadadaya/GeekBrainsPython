import time

class TrafficLight():
    
    __color = 'Red'
    
    def running(self):
        while True:
            __color = 'Red'
            print(__color)
            time.sleep(7)
            __color = 'Yellow'
            print(__color)
            time.sleep(2)
            __color = 'Green'
            print(__color)
            time.sleep(5)

TL = TrafficLight()
TL.running()