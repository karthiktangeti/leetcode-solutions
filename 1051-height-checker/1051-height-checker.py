class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_h[i]:
                count += 1
        return count
        