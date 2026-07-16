# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        current  = head
        while current:
            if current.val in num_set and (current.next is None or current.next.val not in num_set):
                count += 1
            current = current.next
        return count
        