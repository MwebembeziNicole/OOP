class Vehicle:
    def __init__    (self,color):
        self.color = color
        
    def getColor(self):
        return self.color
    
        
    def toString(self):
        print(self.getColor())
        print(f'The vehicle is {self.getColor()}')      
    
if __name__ == '__main__':      
    vehicle1 = Vehicle("red")
    vehicle1.getColor()
    vehicle1.toString()