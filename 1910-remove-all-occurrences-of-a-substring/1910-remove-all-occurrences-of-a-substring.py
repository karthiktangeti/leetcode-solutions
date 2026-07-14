class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for i in s:
            stack.append(i)
            if len(stack) >= m:
                word = "".join(stack)
                if word[-m:] == part:
                    for i in range(m):
                        stack.pop()
        return "".join(stack)
        