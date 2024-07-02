# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nn = ListNode()
        head = nn
        i, j = list1, list2
        while i and j:
            if i.val == j.val:
                nn.next = ListNode(i.val)
                nn = nn.next
                nn.next = ListNode(i.val)
                nn = nn.next
                i, j = i.next, j.next
            elif i.val < j.val:
                nn.next = ListNode(i.val)
                nn = nn.next
                i = i.next
            else:
                nn.next = ListNode(j.val)
                nn = nn.next
                j = j.next
        while i:
            nn.next = ListNode(i.val)
            nn = nn.next
            i = i.next
        while j:
            nn.next = ListNode(j.val)
            nn = nn.next
            j = j.next
        return head.next