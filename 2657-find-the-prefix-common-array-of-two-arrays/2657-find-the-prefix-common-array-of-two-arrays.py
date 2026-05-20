class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        arr = []
        freq = {}
        count = 0
        for i in range(len(A)):
            freq[A[i]] = freq.get(A[i],0) + 1
            if freq[A[i]] == 2:
                count += 1
            
            freq[B[i]] = freq.get(B[i],0) + 1
            if freq[B[i]]  == 2:
                count += 1
            arr.append(count)
        return arr
            

        