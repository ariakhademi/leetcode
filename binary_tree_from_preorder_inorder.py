"""
Given two integer arrays preorder and inorder where preorder 
is the preorder traversal of a binary tree and inorder is the 
inorder traversal of the same tree, construct and return the binary tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None

        # find the root
        root_value = preorder[0]
        root = TreeNode(root_value)

        # look for the root in inorder
        root_idx = inorder.index(root_value)

        # recursive to root's left and right
        root.left = self.buildTree(preorder[1:root_idx + 1],inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

        return root