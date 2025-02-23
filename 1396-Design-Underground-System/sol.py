from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        # how many times and what's the total time for all times
        self.times = defaultdict(lambda : [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station,start_time = self.checkIns.pop(id)
        k = f'{start_station}-{stationName}'
        self.times[k][0] += 1
        self.times[k][1] += t-start_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = f'{startStation}-{endStation}' 
        trips,time = self.times[k]       
        return time / trips

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
