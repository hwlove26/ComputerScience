from typing_extensions import override


class Vehicle():
    #Private ID : STRING
    #Private MaxSpeed : INTEGER
    #Private CurrentSpeed : INTEGER
    #Private IncreaseAmount : INTEGER
    #Private HorizontalPostion : INTGER

    def __init__(self, ID, maxSpeed, increaseAmount):
        self.__ID = ID
        self._MaxSpeed = maxSpeed
        self._IncreaseAmount = increaseAmount
        self._CurrentSpeed = 0
        self._HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self._CurrentSpeed

    def GetIncreaseAmount(self):
        return self._IncreaseAmount

    def GetMaxSpeed(self):
        return self._MaxSpeed

    def GetHorizontalPosition(self):
        return self._HorizontalPosition

    def SetCurrentSpeed(self, speed):
        self._CurrentSpeed = speed

    def SetHorizontalPosition(self, position):
        self._HorizontalPosition = position

    def IncreaseSpeed(self):
        self._CurrentSpeed += self._IncreaseAmount
        if self._CurrentSpeed > self._MaxSpeed:
            self._CurrentSpeed = self._MaxSpeed
        self._HorizontalPosition += self._CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self,ID, MaxSpeed, IncreaseAmount, VerticalChange, MaximumHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalChange = VerticalChange
        self.__MaximumHeight = MaximumHeight
        self.__VerticalPosition = 0

    @override
    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaximumHeight:
            self.__VerticalPosition = self.__MaximumHeight
        self._CurrentSpeed += self._IncreaseAmount
        if self._CurrentSpeed > self._MaxSpeed:
            self._CurrentSpeed = self._MaxSpeed
        self._HorizontalPosition += self._CurrentSpeed

    def GetVerticalPosition(self):
        return self.__VerticalPosition

def GetPosition(vehicle):
    print("The horizontal position of vehicle is " + str(vehicle.GetHorizontalPosition()))
    print("The speed of vehicle is " + str(vehicle.GetCurrentSpeed()))
    if type(vehicle) == Helicopter:
        print("The vertical position of vehicle is " + str(vehicle.GetVerticalPosition()))

def main():
    car = Vehicle("Tiger", 100, 20)
    helicopter = Helicopter("Lion", 350, 40, 3, 100)
    car.IncreaseSpeed()
    car.IncreaseSpeed()
    GetPosition(car)
    helicopter.IncreaseSpeed()
    helicopter.IncreaseSpeed()
    GetPosition(helicopter)

main()



