from class_vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,color,has_winter_tires:bool=False):
        super().__init__(color)
        
        self.has_winter_tires = has_winter_tires
            
    def toString(self):
        return f'The vehicle is {self.getColor()}\nHas winter tires:{self.has_winter_tires}'
    
if __name__ == '__main__':      
    vehicle1 = Car("blue")
    print(vehicle1.toString())    