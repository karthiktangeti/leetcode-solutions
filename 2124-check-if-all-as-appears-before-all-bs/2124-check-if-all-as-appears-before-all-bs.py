class Solution(object):
    def checkString(self, s):
        seen_b = False

        for i in s:
            if i == "b":
                seen_b = True
            if i == "a" and seen_b:
                return False
        return True


        