"""
Given the root of a binary tree, return the average value 
of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""

from collections import deque
import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        ave_arr = []
        queue = deque([root])

        while queue:
            current_level_nodes = []
            current_level_length = len(queue)

            for _ in range(current_level_length):
                node = queue.popleft()
                current_level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ave_arr.append(np.mean(current_level_nodes))

        return ave_arr