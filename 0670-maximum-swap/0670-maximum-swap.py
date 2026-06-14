class Solution(object):
    def maximumSwap(self, num):
        arr = list(str(num))
        last = {}
        for i,d in enumerate(arr):
            last[int(d)] = i
        for i in range(len(arr)):
            for d in range(9,int(arr[i]),-1):
                if d in last and last[d] >  i:
                    j = last[d]
                    arr[i],arr[j] = arr[j],arr[i]
                    return int("".join(arr))
        return num

        