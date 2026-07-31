class Solution(object):
    def findLucky(self, arr):
        des = {}
        for i in arr:
            des[i] = des.get(i,0) + 1
        ans = -1
        for i in arr:
            if des[i] == i:
                if i > ans:
                    ans = i
        return ans
        