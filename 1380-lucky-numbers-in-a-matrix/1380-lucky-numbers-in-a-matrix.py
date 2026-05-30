class Solution(object):
    def luckyNumbers(self, matrix):
        ans = []
        for i in range(len(matrix[0])):
            maxi = float("-inf")
            for j in range(len(matrix)):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
                    r = j
            if maxi == min(matrix[r]):
                ans.append(maxi)
                break
            
        return ans
        
            
            


        