class UndergroundSystem(object):
    def __init__(self):
        self.checkins = {}  
        self.stats = defaultdict(lambda: [0, 0]) 

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start, t0 = self.checkins[id]
        key = (start, stationName)

        self.stats[key][0] += (t - t0)
        self.stats[key][1] += 1

        del self.checkins[id]

    def getAverageTime(self, startStation, endStation):
        total, count = self.stats[(startStation, endStation)]
        return float(total) / count
       


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)