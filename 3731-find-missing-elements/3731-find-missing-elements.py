class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minEl = nums[0]

        missing = []
        for i in nums:
            while i != minEl:
                missing.append(minEl)
                minEl += 1
            else:
                minEl += 1
        return missing
            
                
        