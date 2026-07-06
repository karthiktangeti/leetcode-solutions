class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l,r = 0,len(letters) - 1
        ans = letters[0]
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans
        