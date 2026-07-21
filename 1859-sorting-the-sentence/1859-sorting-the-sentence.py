class Solution(object):
    def sortSentence(self, s):
        res = list(s.split(" "))
        ans = [0] * len(res)
        for i in res:
            ans[int(i[-1]) - 1] = i[:-1]
        return " ".join(ans)
              