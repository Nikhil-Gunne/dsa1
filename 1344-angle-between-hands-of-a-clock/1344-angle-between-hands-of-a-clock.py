class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hoursAngle = ((hour * 30) %360) + (minutes/12) * 6
        minutesAngle = minutes * 6
        # print(hourspos,minutespos)
        diffAngle = abs(hoursAngle-minutesAngle)
        return min(360-diffAngle,diffAngle)

        