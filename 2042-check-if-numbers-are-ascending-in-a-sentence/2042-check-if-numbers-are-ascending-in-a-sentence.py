class Solution(object):
    def areNumbersAscending(self, s):
        arr = []
        for ch in s.split():
            if ch.isdigit():
                arr.append(int(ch))
        for  i in range(1,len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True
        
        