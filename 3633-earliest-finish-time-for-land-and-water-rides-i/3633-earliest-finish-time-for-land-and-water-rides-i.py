class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        lRides = [(landStartTime[i],landStartTime[i]+landDuration[i]) for i in range(len(landStartTime))]
        wRides = [(waterStartTime[i],waterStartTime[i]+waterDuration[i]) for i in range(len(waterStartTime))]

        
        minTime = float('inf')
        for i in range(len(lRides)):
            start,end = lRides[i][0],lRides[i][1]
            for j in range(len(wRides)):
                if wRides[j][0] >= end:
                    minTime = min(minTime,wRides[j][1])
                elif wRides[j][1] < start:
                    minTime = min(minTime,end)
                else:
                    minTime = min(minTime,end+(wRides[j][1]-wRides[j][0]))
        lRides,wRides = wRides,lRides
        for i in range(len(lRides)):
            start,end = lRides[i][0],lRides[i][1]
            for j in range(len(wRides)):
                if wRides[j][0] >= end:
                    minTime = min(minTime,wRides[j][1])
                elif wRides[j][1] < start:
                    minTime = min(minTime,end)
                else:
                    minTime = min(minTime,end+(wRides[j][1]-wRides[j][0]))
        return minTime
                    
                    

