class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        free = []
        opens = []
        for i in range(len(s)):
            if locked[i] == "0":
                free.append(i)
            elif s[i] == "(":
                opens.append(i)
            else:
                if opens:
                    opens.pop()
                elif free:
                    free.pop()
                else:
                    return False
        while free and opens:
            if opens[-1] < free[-1]:
                free.pop()
                opens.pop()
            else:
                return False
        return len(opens) == 0
        