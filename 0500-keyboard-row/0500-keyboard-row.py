class Solution(object):
    def findWords(self, words):
        f = "qwertyuiopQWERTYUIOP"
        s = "asdfghjklASDFGHJKL"
        t = "zxcvbnmZXCVBNM"
        arr =[]
        for i in words:
            k,l,m = 0,0,0
            for j in i:
                if j in f:
                    k = 1
                else:
                    k = 0
                    break
            for j in i:
                if j in s:
                    l = 1
                else:
                    l = 0
                    break
            for j in i:
                if j in t:
                    m = 1
                else:
                    m = 0
                    break
            if k or l or m:
                arr.append(i)
        return arr            
        

