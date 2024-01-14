class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        s = arrivalTime + delayedTime

        if s == 24:
            return 0

        while s > 24:
            s = s - 24

        return s