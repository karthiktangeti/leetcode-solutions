class Solution(object):
    def lexicalOrder(self, n):
        result = []
        def dfs(curr):
            if curr > n:
                return 
            result.append(curr)
            for i in range(10):
                new_num = curr * 10 + i
                if new_num > n:
                    return 
                dfs(new_num)
        for i in range(1,10):
            dfs(i)
        return result
        