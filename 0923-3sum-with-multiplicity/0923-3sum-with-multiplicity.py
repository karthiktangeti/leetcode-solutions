class Solution(object):
    def threeSumMulti(self, arr, target):
        arr.sort()
        ans = 0
        n = len(arr)
        MOD = 10 ** 9 + 7
        for i in range(n):
            t = target - arr[i]
            left = i + 1
            right = n -1
            while left < right:
                s = arr[left] + arr[right]

                if s < t:
                    left += 1
                elif s > t:
                    right -=1
                else:
                    if arr[left] != arr[right]:
                        leftcount = 1
                        rightcount = 1

                        while left + 1 < right and arr[left] == arr[left + 1]:
                            leftcount += 1
                            left += 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            rightcount += 1
                            right -= 1
                        ans += rightcount * leftcount
                        left += 1
                        right -= 1
                    else:
                        m = right - left + 1
                        ans += m * (m - 1) // 2
                        break
        return ans % MOD
