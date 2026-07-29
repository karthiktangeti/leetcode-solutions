from collections import defaultdict
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        memo = {}
        def dfs(co):
            if co in memo:
                return memo[co]
            reach = set()
            for nei in graph[co]:
                reach.add(nei)
                reach |= dfs(nei)
            memo[co] = reach
            return reach
        for i in range(numCourses):
            dfs(i)
        ans =[]
        for u,v in queries:
            ans.append(v in memo[u])
        return ans
       

        