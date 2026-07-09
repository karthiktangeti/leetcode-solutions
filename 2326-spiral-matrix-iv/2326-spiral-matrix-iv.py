# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        matrix= [[-1] * n for i in range(m)]
        l = 0
        r = n -1
        t = 0
        b = m - 1
        while head and l <= r and t <= b:
            for i in range(l,r + 1):
                if not head:
                    break
                matrix[t][i] = head.val
                head = head.next
            t += 1
            for i in range(t,b + 1):
                if not head:
                    break
                matrix[i][r] = head.val
                head = head.next
            r -= 1
            if t <= b:
                for i in range(r ,l - 1,-1):
                    if not head:
                        break
                    matrix[b][i] = head.val
                    head = head.next
                b -= 1
            if l <= r:
                for i in range(b,t-1,-1):
                    if not head:
                        break
                    matrix[i][l] = head.val
                    head = head.next
                l += 1
        return matrix

                
        