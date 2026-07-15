class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        des = {}
        end = {}
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in des:
                des[nums[i]] = i
            end[nums[i]] = i
            freq[nums[i]] = freq.get(nums[i],0) + 1
        degree = max(freq.values())
        ans = len(nums)
        for i in freq:
            if freq[i] == degree:
                ans = min(ans,end[i] - des[i] + 1)
        return ans

        
            
            
        