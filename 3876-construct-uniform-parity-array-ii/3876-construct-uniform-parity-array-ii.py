class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for x in nums1:
            if x % 2:
                minOdd = min(minOdd, x)
            else:
                minEven = min(minEven, x)
        #case where there are no odd numbers. all are even
        if minOdd == float('inf'):
            return True

        #if the smallest number in nums1 is odd then it is impossible to convert to all evens.can only be converted to all odds.
        
        return minEven > minOdd