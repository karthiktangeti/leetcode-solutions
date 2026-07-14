class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                for i in temp:
                    stack.append(i)
        return "".join(stack)
        