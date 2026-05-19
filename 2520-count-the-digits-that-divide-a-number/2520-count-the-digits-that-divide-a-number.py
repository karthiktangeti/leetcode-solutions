class Solution(object):
    def countDigits(self, num):
        arr = [int(x) for x in str(num)]
        count = 0
        for i in arr:
            if num % i == 0:
                count += 1
        return count
        