class Solution(object):
    def intersection(self, nums):
        des = {}
        for i in nums:
            for j in i:
                des[j] = des.get(j,0) + 1
        ans = []
        for key in des:
            if des[key] == len(nums):
                ans.append(key)
        ans.sort()
        return ans
        
            
        