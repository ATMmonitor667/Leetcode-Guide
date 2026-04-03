class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
            n = len(stations)
            dp = [0] * (n + 1)
            dp[0] = startFuel
            for i in range(n):
                station_pos, station_fuel = stations[i]
                for t in range(i, -1, -1): 
                    if dp[t] >= station_pos:    
                        dp[t + 1] = max(dp[t + 1], dp[t] + station_fuel)   
            for stops in range(n + 1):
                if dp[stops] >= target:
                    return stops
            return -1