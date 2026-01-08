class ParkingSystem:
    def __init__(self, big, medium, small):
        self.spots = [0, big, medium, small]  # index by carType

    def addCar(self, carType):
        if self.spots[carType] == 0:
            return False
        self.spots[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)