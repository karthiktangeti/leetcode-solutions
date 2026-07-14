class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        operations = []
        j = 0
        for i in range(1,n + 1):
            if j == len(target):
                break
            if target[j] == i:
                stack.append(i)
                operations.append("Push")
                j += 1
            else:
                stack.append(i)
                operations.append("Push")

                stack.pop()
                operations.append("Pop")
        return operations

        