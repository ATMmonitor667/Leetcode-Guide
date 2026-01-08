class ParkingSystem(object):
    

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.container = []
        self.container.append(big)
        self.container.append(medium)
        self.container.append(small)

        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        
        #lookUp = len(container) - cirr
        if self.container[carType-1] == 0:
            return False
        if self.container[carType-1] !=0:
            self.container[carType-1]-=1
            return True

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)