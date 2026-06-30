class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index,path):
            if len(path) >= 2:
                result.append(path[:])
            used = set()
            for i in range(index,len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1,path)
                    path.pop()
        dfs(0,[])
        return result