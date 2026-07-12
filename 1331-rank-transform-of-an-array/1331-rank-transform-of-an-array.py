class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        des = {}
        sorted_arr = sorted(list(set(arr)))
        for i in range(len(sorted_arr)):
            des[sorted_arr[i]] = i + 1
        for i in range(len(arr)):
            arr[i] = des[arr[i]]
        return arr

        