class Solution(object):
    def numTilePossibilities(self, tiles):
        res = set()
        used = [False] * len(tiles)
        def dfs(path):
            if path:
                res.add("".join(path))
            for i in range(len(tiles)):
                if used[i]:
                    continue
                used[i] = True
                path.append(tiles[i])
                dfs(path)
                path.pop()
                used[i] = False
        dfs([])
        return len(res)
        