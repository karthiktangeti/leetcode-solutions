class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        l = 0
        n = len(arr)
        target = k * threshold
        sum1 = 0
        count = 0
        for i in range(n):
            sum1 += arr[i]
            if i - l == k:
                sum1 -= arr[l]
                l += 1
            if i - l + 1 == k:
                if sum1 >= target:
                    count += 1
        return count
