class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        
        # Step 1: sort
        sorted_nums = sorted(nums)
        
        # Step 2: split into two halves
        mid = (n + 1) // 2
        small = sorted_nums[:mid][::-1]   # reverse
        large = sorted_nums[mid:][::-1]   # reverse
        
        # Step 3: place alternately
        nums[::2] = small   # even indices
        nums[1::2] = large  # odd indices