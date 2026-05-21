class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        prifix = set()
        for num in arr1:
            while num > 0:
                prifix.add(num)
                num //= 10
        ans = 0
        for num in arr2:

            while num > 0:
                if num in prifix:
                    ans = max(ans,len(str(num)))

                    break
                num //= 10
        return ans
    