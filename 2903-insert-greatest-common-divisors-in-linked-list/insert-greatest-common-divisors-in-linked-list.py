# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next != None:
            nn = ListNode(gcd(temp.val, temp.next.val))
            nn.next = temp.next
            temp.next = nn
            temp = nn.next
        return head

        
        