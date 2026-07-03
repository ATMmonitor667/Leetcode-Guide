class UndergroundSystem(object):

    def __init__(self):
        self.place = {}
        self.customer = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id in self.customer:
            print("already been here man")
            return

        self.customer[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.customer:
            return

        prevLocation, prevt = self.customer[id]
        totalTime = t - prevt

        if (prevLocation, stationName) in self.place:
            currTotal, currCount = self.place[(prevLocation, stationName)]
            currTotal += totalTime
            currCount += 1
            self.place[(prevLocation, stationName)] = (currTotal, currCount)
        else:
            self.place[(prevLocation, stationName)] = (totalTime, 1)

        del self.customer[id]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        totalTime, totalCount = self.place[(startStation, endStation)]
        return float(totalTime) / totalCount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)