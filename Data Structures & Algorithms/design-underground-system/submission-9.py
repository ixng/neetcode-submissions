from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.trips = {} # key = id , value = start station,start time
        self.routes = {} # key = start,end . value  = total time, trip count for that route
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName,t)    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.trips.pop(id)
        route = (startStation, stationName)
        if route not in self.routes:
            self.routes[route] = [t - startTime, 1]
        else:
            self.routes[route][0] += t - startTime
            self.routes[route][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routes[route][0] / self.routes[route][1]
        
