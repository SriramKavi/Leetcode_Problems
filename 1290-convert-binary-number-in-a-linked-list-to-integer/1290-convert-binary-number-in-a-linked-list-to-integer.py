# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        n = 0
        while temp != None:
            n += 1
            temp = temp.next
        n = n - 1
        t = head
        res = 0
        while t != None:
            if t.val == 1:
                res += (1 << n)
            n = n - 1
            t = t.next
        return res
            