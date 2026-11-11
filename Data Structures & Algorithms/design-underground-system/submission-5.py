from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.trips = {} # key = id , value = start station,start time
        self.routes = defaultdict(tuple) # key = start,end . value  = total time, trip count for that route
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = [stationName,t]    
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.trips[id][0]
        startTime = self.trips[id][1]
        if not self.routes[(startStation, stationName)]:
            self.routes[(startStation, stationName)] = [t - startTime, 1]
        else:
            self.routes[(startStation, stationName)][0] += t - startTime
            self.routes[(startStation, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return routes[(startStation,endStation)][0] / routes[(startStation,endStation)][1]
        
