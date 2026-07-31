class Solution(object):
    def minimumPushes(self, word):
        fre = [0] * 26
        for c in word:
            fre[ord(c) - ord("a")] += 1
        pa = 0
        fre.sort(reverse = True)
        for i in range(26):
            if fre[i] == 0:
                break
            pa += (i // 8 + 1) * fre[i]
        return pa
        