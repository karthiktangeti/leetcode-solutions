# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        for i in range(0,len(arr),k):
            if i + k <= len(arr):
                arr[i:i+k] = arr[i:i+k][::-1]
        dummy = ListNode(0)
        curr = dummy
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next