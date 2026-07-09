# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        def dfs(leftNode, rightNode, level):
            if not leftNode or not rightNode:
                return

            # Reverse values at odd levels
            if level % 2 == 1:
                leftNode.val, rightNode.val = rightNode.val, leftNode.val

            # Move to the next level
            dfs(leftNode.left, rightNode.right, level + 1)
            dfs(leftNode.right, rightNode.left, level + 1)

        if root:
            dfs(root.left, root.right, 1)

        return root
        