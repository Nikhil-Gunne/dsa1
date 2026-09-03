class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minEl = min(nums1)
        # if minimum element is odd then it is always possible to create all odds.
        if minEl % 2 == 1:
            return True
        #if minimum element is even then we can have only all evens.if there are any odds we cannot convert all the odds to even
        for i in nums1:
            if i & 1:
                return False
        return True
        # minOdd = float('inf')
        # minEven = float('inf')

        # for x in nums1:
        #     if x % 2:
        #         minOdd = min(minOdd, x)
        #     else:
        #         minEven = min(minEven, x)
        # #case where there are no odd numbers. all are even
        # if minOdd == float('inf'):
        #     return True

        # #if the smallest number in nums1 is odd then it is impossible to convert to all evens.can only be converted to all odds.

        # return minEven > minOdd