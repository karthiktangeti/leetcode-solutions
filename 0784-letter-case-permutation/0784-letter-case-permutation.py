class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def dfs(i,res):
            if i == len(s):
                ans.append(res)
                return
            if s[i].isdigit():
                dfs(i + 1,res + s[i])
            else:
                dfs(i + 1,res + s[i].lower())
                dfs(i + 1,res + s[i].upper())
        dfs(0,"")
        return ans
        