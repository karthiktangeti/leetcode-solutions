class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        count = 0
        arr = []
        for i in range(len(rocks)):
            diff = capacity[i] - rocks[i]
            if diff == 0:
                count +=1
            else:
                arr.append(diff)
        arr.sort()
        i = 0
        while i < len(arr):
            if arr[i] <= additionalRocks:
                additionalRocks -= arr[i]
                count += 1
            else:
                break
            i += 1
        return count
        
        