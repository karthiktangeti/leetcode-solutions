class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = [[] for i in range(n)]
        for rich,poor in richer:
            graph[poor].append(rich)
        ans = [-1] * n
        def dfs(person):
            if ans[person] != -1:
                return ans[person]
            ans[person] = person
            for rich in graph[person]:
                can = dfs(rich)
                if quiet[can] < quiet[ans[person]]:
                    ans[person] = can
            return ans[person]
        for i in range(n):
            dfs(i)
        return ans
        