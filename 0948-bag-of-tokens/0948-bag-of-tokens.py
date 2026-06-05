class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score = 0
        l = 0
        r = len(tokens) - 1
        ans = 0
        while l  <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                ans = max(ans,score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return ans

        
        