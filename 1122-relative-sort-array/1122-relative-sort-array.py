class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        des = {}
        for i in arr1:
            if i not in des:
                des[i] = []
                des[i].append(i)
            else:
                des[i].append(i)
        res = []
        for i in arr2:
            res.extend(des[i])
            del des[i]
        for i in dict(sorted(des.items())):
            res.extend(des[i])
        return res