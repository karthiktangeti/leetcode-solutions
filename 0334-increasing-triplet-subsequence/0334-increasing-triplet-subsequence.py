class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num          # smallest
            elif num <= second:
                second = num         # second smallest
            else:
                return True          # found third > first & second

        return False