class Car(object):
    condition = 'new'
    def __init__ (self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        print(self.model, self.color, self.mpg)
        
    def display_car(self):
        print('This is a ' + self.color + self.model + 'with' + str(self.mpg) + 'MPG')
        
    def drive_car(self):
        self.condition = 'used'
        print(self.condition)
        
class ElectricCar(Car):
    def __init__ (self, model, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
        
        def description(self):
            print(self.model, self.color, self.mpg, self.battery_type)
            
        def drive_car(self):
            condition = 'like new'
            
my_car = Car('Chevy', 'green', '22')
e_car = ElectricCar('Toyota', 'brown', '56', 'molten salt')
my_car.display_car()
my_car.drive_car()