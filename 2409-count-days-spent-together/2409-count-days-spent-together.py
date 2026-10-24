class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        commonStart = max(arriveAlice, arriveBob)
        commonEnd = min(leaveAlice, leaveBob)

        if commonStart > commonEnd:
            return 0

        startMonth, startDay = map(int, commonStart.split('-'))
        endMonth, endDay = map(int, commonEnd.split('-'))

        if startMonth == endMonth:
            return endDay - startDay + 1

        days = month_days[startMonth - 1] - startDay + 1

        for month in range(startMonth + 1, endMonth):
            days += month_days[month - 1]

        days += endDay

        return days