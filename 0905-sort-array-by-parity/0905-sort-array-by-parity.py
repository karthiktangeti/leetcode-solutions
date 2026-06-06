class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        even.extend(odd)
        return even

        