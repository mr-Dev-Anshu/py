class Car :
    def __init__(self , brand , model ):
        self.brand = brand 
        self.model = model 

class ElectricCar(Car) :
    def __init__(self , brand , model , battrySize ):
        super().__init__(brand,model)
        self.battrySize = battrySize


myTesla = ElectricCar("Tesla","S" , "85wh")

print(myTesla.battrySize)