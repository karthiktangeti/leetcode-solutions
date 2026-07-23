class Solution(object):
    def canVisitAllRooms(self, rooms):
        total = len(rooms)
        visited = total * [False]
        def dfs(room):
            visited[room] = True
            for i in rooms[room]:
                if not visited[i]:
                    dfs(i)
        dfs(0)
        return all(visited)
        