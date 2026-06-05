class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x : x[1],reverse = True)
        sum1 = 0 
        count = 0
        for i in range(len(boxTypes)):
            x,y = boxTypes[i]
            sum1 += x
            if sum1 < truckSize:
                count += x * y
            if sum1 >= truckSize:
                diff = sum1 - truckSize
                count += (x - diff) * y
                break
        return count


        