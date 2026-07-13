class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        des = {}
        for i in arr:
            des[i] = des.get(i,0) + 1
        res = []
        for key in des:
            res.append(des[key])
        res.sort()
        for i in range(1,len(res)):
            if res[i] == res[i - 1]:
                return False
        return True