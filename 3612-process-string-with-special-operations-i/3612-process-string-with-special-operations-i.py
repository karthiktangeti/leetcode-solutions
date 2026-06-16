class Solution(object):
    def processStr(self, s):
        r = ""
        ans = []
        for i in s:
            if i.isalpha():
                ans.append(i)
            elif i == "#":
                ans.extend(ans)
            elif i == "%":
                ans = ans[::-1]
            elif i == "*":
                if ans:
                    ans.pop()
        return "".join(ans)
                
            
        