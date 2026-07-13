class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increse = True
        decrese = True
        for i in range(1,len(nums)):
            if nums[i] < nums[i -1]:
                increse = False
            if nums[i] > nums[i - 1]:
                decrese = False
        return increse or decrese