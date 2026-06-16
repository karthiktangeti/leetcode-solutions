# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kh = group_prev
            for i in range(k):
                kh = kh.next
                if not kh:
                    return dummy.next
            group_next = kh.next
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = group_prev.next
            group_prev.next = kh
            group_prev = temp
    