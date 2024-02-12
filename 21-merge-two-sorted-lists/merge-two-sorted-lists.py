# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nn = ListNode(None)
        p = nn
        i = list1
        j = list2
        while i != None and j != None:
            if i.val <= j.val:
                nn.next = i
                nn = nn.next
                i = i.next
            else:
                nn.next = j
                nn = nn.next
                j = j.next
        while i != None:
            nn.next = i
            nn = nn.next
            i = i.next
        while j != None:
            nn.next = j
            nn = nn.next
            j = j.next
        p = p.next
        return p
