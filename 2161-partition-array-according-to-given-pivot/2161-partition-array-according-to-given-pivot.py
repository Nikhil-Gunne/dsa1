class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot] * n
        left = 0
        right = n-1
        for i in range(n):
            if nums[i] < pivot:
                res[left] = nums[i]
                left+=1
            if nums[n-i-1] > pivot:
                res[right] = nums[n-i-1]
                right-=1
        return res
