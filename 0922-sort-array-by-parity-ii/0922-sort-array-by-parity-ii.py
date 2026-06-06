class Solution(object):
    def sortArrayByParityII(self, nums):
        nums.sort()
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        e = 0
        odd.sort()
        o = 0
        res = []
        for i in range(len(nums)):
            if i % 2 == 0 and e != len(even):
                res.append(even[e])
                e += 1

            elif i % 2 and o != len(odd):
                res.append(odd[o])
                o += 1

        return res
            
        

        