class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        ans = 0
        for x in arr1:
            left = 0
            right = len(arr2) - 1
            found = False
            while left <= right:
                mid = (left + right) // 2
                if (abs(arr2[mid] - x) <= d):
                    found = True
                    break
                elif arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            if not found:
                ans += 1
        return ans


        
        