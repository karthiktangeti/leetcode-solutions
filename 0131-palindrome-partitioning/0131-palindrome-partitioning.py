class Solution(object):
    def partition(self, s):
        res = []
        def palindrom(sub):
            return sub == sub[::-1]
        def dfs(start,path):
            if start == len(s):
                res.append(path[:])
                return 
            for i in range(start,len(s)):
                curr = s[start:i + 1]
                if palindrom(curr):
                    path.append(curr)
                    dfs(i + 1,path)
                    path.pop()
        dfs(0,[])
        return res