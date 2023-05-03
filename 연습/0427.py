"""
class data:
    __a = 10
    b = "b"
    
    def __init__(self) :
        self.__a = 20
    
    def method(self) :
        return self.__a
    
d = data()

print(d.method())

"""

"""
class Car:
    maxSpeed = 0
    price = 0
    __engine = ""
    carName = ""
    
    def __init__(self, p, name) :
        price = p
        carName = name
        print("============")
        print("car price :", price, "car name :", carName)
    
    def goFoward(self) :
        print("going forward", self.maxSpeed)
    
    def goBackward(self) :
        print("going backward", int(self.maxSpeed / 2))
        
    def stop(self) :
        print("stop")
        
    def startMusic(self, name) :
        print("playing music :", name)
        
    def getEngine(self) :
        return self.__engine
        
    def setEngine(self, name) :
        self.__engine = name
    
    def __del__(self) :
        print("car Crashed!")
        print("============")
        
#car1 = Car(int(input("Car price : ")), input("Car name : "))
car1 = Car(100, "corvette")

car1.maxSpeed = 10

car1.goFoward()
car1.goBackward()
car1.stop()
car1.startMusic("highway to hell")
car1.setEngine("GM 7.0 Liter V8 LS7 Engine")

print(car1.getEngine())

del(car1)
"""

class Vehicle:
    __maxSpeed = 0
    __name = ""
    VehicleID = ""
    
    def __init__(self, ID) :
        self.VehicleID = ID
        
    def __add__(self, other) :
        print(f"{self.__name}과 {other.__name}가 충돌했습니다.")
    
    def goForward(self) :
        print(self.__name, "is going forward :", self.__maxSpeed)
    
    def goBackward(self) :
        print(self.__name, "going backward :", self.__maxSpeed / 2)
    
    def stop(self) :
        print("stop!")
    
    def getMaxSpeed(self) :
        return self.__maxSpeed
    
    def getName(self) :
        return self.__name
    
    def setMaxSpeed(self, speed) :
        self.__maxSpeed = speed
    
    def setName(self, name) :
        self.__name = name
    
    def __del__(self) :
        print(self.__name, "CRASH")

class Car(Vehicle) :
    engine = ""
    
    def __init__(self, ID, value) :
        self.VehicleID = ID
        self.engine = value
        
    def goForward(self) :
        print("going forward :", 21)
    
    """#오버라이딩?
    def __del__(self) :
        print("도망가~")"""
    

class Bike(Vehicle) :
    wheelCnt = 0
    
    def __init__(self, ID) :
        self.VehicleID = ID
        self.wheelCnt = 2

car1 = Car("AABB11", "V8")

car1.setMaxSpeed(100)
car1.setName("Corvette")

car1.goForward()
car1.goBackward()

print(car1.getName(), car1.engine)

bike1 = Bike("BBCC22")

bike1.setMaxSpeed(80)
bike1.setName("kawasaki")

bike1.goForward()
bike1.goBackward()

print(bike1.getName(), bike1.wheelCnt)

car1 + bike1

print(bike1.getName())

super(Car, car1).goForward()