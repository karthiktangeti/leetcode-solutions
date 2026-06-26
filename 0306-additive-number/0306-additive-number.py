class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        def dfs(fis,sec,index):
            if index == n:
                return True
            third = fis + sec
            third_str = str(third)
            if not num.startswith(third_str,index):
                return False

            return dfs(sec,third,index + len(third_str))
        for i in range(1,n):
            if num[0] == "0" and i > 1:
                break
            first = int(num[:i])
            for j in range(i+1,n):
                if num[i] == "0" and j - i > 1:
                    break
                second = int(num[i:j])
                if dfs(first,second,j):
                    return True
        return False


        