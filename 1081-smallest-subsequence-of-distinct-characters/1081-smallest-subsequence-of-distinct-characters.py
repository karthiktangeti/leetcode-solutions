class Solution(object):
    def smallestSubsequence(self, s):
        last_num ={}
        for i,ch in enumerate(s):
            last_num[ch] = i
        stack =[]
        used = set()
        for i,ch in enumerate(s):
            if ch in used:
                continue
            while stack and ch < stack[-1] and last_num[stack[-1]] > i:
                remove = stack.pop()
                used.remove(remove)
            stack.append(ch)
            used.add(ch)
        return "".join(stack)