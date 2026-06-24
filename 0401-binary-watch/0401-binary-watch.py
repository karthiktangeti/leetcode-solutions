class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        arr = [8,4,2,1,32,16,8,4,2,1]
        ans = []
        def dfs(index,remain,hour,minutes):
            if hour > 11 or minutes > 59:
                return 
            if remain == 0:
                ans.append(f"{hour}:{minutes:02d}")
                return 
            for i in range(index,10):
                if i < 4:
                    dfs(i + 1,remain - 1,hour + arr[i],minutes)
                else:
                    dfs(i + 1,remain - 1,hour,minutes + arr[i])
        dfs(0,turnedOn,0,0)
        return ans