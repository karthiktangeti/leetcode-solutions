class Solution(object):
    def candy(self, ratings):
        sum1 = 1 
        i = 1
        if len(ratings) == 0:
            return 0
        while i < len(ratings):
            if ratings[i] == ratings[i- 1]:
                sum1 += 1
                i += 1
                continue
            peek = 1
            while (i < len(ratings)) and (ratings[i] > ratings[i-1]):
                peek += 1
                sum1 += peek
                i += 1
            down = 1
            while (i < len(ratings)) and (ratings[i] < ratings[i - 1]):
                sum1 += down
                down += 1
                i += 1
            if down > peek:
                sum1 += down - peek
        return sum1

        