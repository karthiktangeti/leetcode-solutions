class Solution(object):
    def secondHighest(self, s):
        arr = []
        for i in s:
            if i.isdigit():
                arr.append(int(i))
        arr = list(set(arr))
        if len(arr) < 2:
            return -1
        else:
            arr.sort()
            return arr[-2]
        