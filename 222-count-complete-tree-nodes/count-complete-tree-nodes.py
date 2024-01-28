# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count_Nodes(self, root):
        if root == None:
            return 0
        return 1 + self.count_Nodes(root.left) + self.count_Nodes(root.right)


    def countNodes(self, root: Optional[TreeNode]) -> int:
        a = self.count_Nodes(root)
        return a

        