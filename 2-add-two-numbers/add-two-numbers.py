# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        carry = 0
        nn = ListNode(None)
        head = nn
        while l1 and l2:
            s = l1.val + l2.val + carry
            nn.next = ListNode(s % 10)
            nn = nn.next
            carry = s // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + carry
            nn.next = ListNode(s % 10)
            nn = nn.next
            carry = s // 10
            l1 = l1.next
        while l2:
            s = l2.val + carry
            nn.next = ListNode(s % 10)
            nn = nn.next
            carry = s // 10
            l2 = l2.next
        if carry: nn.next = ListNode(carry)
        return head.next