# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def suf(self, root, s):
        if(root.left == None and root.right == None):
           lst.append(int(s + str(root.val)))
           return
        if(root.left != None):
            self.suf(root.left, s + str(root.val))
        if(root.right != None):
            self.suf(root.right, s + str(root.val))


        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global lst
        lst = []
        self.suf(root, "")
    
        return sum(lst)
