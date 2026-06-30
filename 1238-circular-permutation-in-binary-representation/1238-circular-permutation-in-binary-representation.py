class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = []
        for i in range(1 << n):
            gray.append(i ^ (i >> 1))
        idx = gray.index(start)
        return gray[idx:] + gray[:idx]