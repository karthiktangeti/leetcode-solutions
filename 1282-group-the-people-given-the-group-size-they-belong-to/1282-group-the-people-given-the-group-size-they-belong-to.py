class Solution(object):
    def groupThePeople(self, groupSizes):
        dist = {}
        arr = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dist:
                dist[groupSizes[i]] = []
                dist[groupSizes[i]].append(i)
            else:
                dist[groupSizes[i]].append(i)
        for size,val in dist.items():
            for i in range(0,len(val),size):
                arr.append(val[i:i+size])
        return arr
