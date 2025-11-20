from heapq import heappush,heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  
        event = 0
        attended = 0
        sz = len(events)
        day = 1
        mnHeap = []
        while event < sz or mnHeap:
            # remove finished events
            while len(mnHeap) > 0 and mnHeap[0] < day:
                heappop(mnHeap)
            # optimization (jump to the next event if there are no ones left) 
            # instead of moving 1 by 1
            # if event < sz and len(mnHeap) == 0:
            #     day = max(day,events[event][0])
            # add active events today
            while event < sz and events[event][0] == day:
                heappush(mnHeap,events[event][1])
                event +=1

            
            # attend the one ending first
            if len(mnHeap) > 0:
                attended +=1
                heappop(mnHeap)
            day+=1
        return attended