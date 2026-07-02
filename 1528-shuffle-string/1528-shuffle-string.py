class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(s)
        for i in range(len(arr)):
            arr[indices[i]] = s[i]
        return "".join(arr)

        