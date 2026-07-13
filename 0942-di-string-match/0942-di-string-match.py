class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        arr = []
        for i in s:
            if i == "I":
                arr.append(low)
                low += 1
            else:
                arr.append(high)
                high -= 1
        arr.append(low)
        return arr
