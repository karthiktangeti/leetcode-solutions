class Solution(object):
    def sortEvenOdd(self, nums):
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse = True)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop(0)
            else:
                nums[i] = odd.pop(0)
        return nums
        
        
        