class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        arr = [0] * n
    
        if k == 0:
            return [0] * n
        if k > 0:
            window_sum =0
            for i in range(1,k + 1):
                window_sum += code[i % n]
            for i in range(n):
                arr[i] = window_sum
                window_sum -= code[(1 + i )% n]
                window_sum += code[(i + k + 1) % n]
        else:
            k = -k
            window_sum = 0
            for i in range(n - k,n):
                window_sum += code[i]
            for i in range(n):
                arr[i] = window_sum
                window_sum -= code[(i - k + n)% n]
                window_sum += code[i]
        return arr