# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        temp = head
        lenght = 0
        while temp:
            lenght += 1
            temp = temp.next
        tmp = dummy
        for i in range(lenght - n):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return dummy.next

        