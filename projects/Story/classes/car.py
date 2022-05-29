class Car:

    def __init__(
            self,
            carName=None,
            fuelRate=100,
            velocity=60
    ):
        self._carName = carName
        self._fuelRate = fuelRate
        self._velocity = velocity

    @property
    def carName(self):
        return self._carName

    @carName.setter
    def carName(self, name):
        self._carName = name

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate):
        self._fuelRate = fuelRate

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    def run(self, velocity=60, distance=20):
        self.velocity = velocity
        while distance != 0:
            self.fuelRate = self._fuelRate - (self.fuelRate * 0.01)
            self.fuelRate = int(self._fuelRate)
            distance -= 1
            if distance == 0:
                print("Arrived .. welcome in office :)")
                self.stop()
                return distance
            if self._fuelRate <= 0:
                print(f"Fuel out.. remaining distance: {distance}")
                self.stop()
                return distance

    def stop(self):
        self.velocity = 0

# test Car class
# if __name__ == '__main__':
    # car = Car("Fiat", 100, 0)
    # print(car.carName)
    # print(car.run(60, 20))
    # print(car.fuelRate)
