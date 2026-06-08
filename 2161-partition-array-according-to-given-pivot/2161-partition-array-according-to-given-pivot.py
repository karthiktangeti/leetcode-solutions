class Solution(object):
    def pivotArray(self, nums, pivot):
        le = []
        ri = [] 
        same = 0
        for i in nums:
            if i == pivot:
                same += 1

            if i < pivot:
                le.append(i)
            elif i != pivot:
                ri.append(i)
        for i in range(same):
            le.append(pivot)
        le.extend(ri)
        return le