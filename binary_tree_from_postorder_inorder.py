"""
Given two integer arrays inorder and postorder where 
inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, 
construct and return the binary tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder or not postorder:
            return None

        # extract root
        root_value = postorder[-1]
        root = TreeNode(root_value)
        
        # look for root index in inorder
        root_idx = inorder.index(root_value)

        # build the left and right sub-trees
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx:-1])

        return root