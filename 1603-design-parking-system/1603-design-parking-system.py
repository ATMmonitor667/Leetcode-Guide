class ParkingSystem(object):
    

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.container = []
        self.container += [big, medium, small]
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        carType = carType - 1
        #lookUp = len(container) - cirr
        if self.container[carType] == 0:
            return False
        if self.container[carType] !=0:
            self.container[carType]-=1
            return True

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)