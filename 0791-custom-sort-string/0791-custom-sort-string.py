class Solution(object):
    def customSortString(self, order, s):
        rank = {}
        for i in range(len(order)):
            rank[order[i]] = i
        arr = list(s)
        arr.sort(key = lambda ch :rank.get(ch,float("inf")))
        return "".join(arr)
        