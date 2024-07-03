# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            flag = False
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                flag = True
            if not flag: prev = curr
            else:
                if prev: prev.next = curr.next
                else: head = curr.next
            curr = curr.next
        return head