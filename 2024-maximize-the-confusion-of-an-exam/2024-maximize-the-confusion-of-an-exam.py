class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        t_count = 0
        f_count = 0
        ans =0
        l = 0
        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                t_count += 1
            else:
                f_count += 1
            while min(t_count,f_count) > k:
                if answerKey[l] == "T":
                    t_count -= 1
                else:
                    f_count -= 1
                l += 1
            ans = max(ans,i - l + 1)
        return ans