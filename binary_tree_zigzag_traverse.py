"""
Given the root of a binary tree, return the zigzag level order 
traversal of its nodes' values. (i.e., from left to right, 
then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        left_to_right = True
        res = []
        queue = deque([root])

        while queue:
            level_arr = []
            current_level_length = len(queue)

            if left_to_right: 
                for _ in range(current_level_length):
                    node = queue.popleft()
                    level_arr.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                res.append(level_arr)
                
            else: 
                for _ in range(current_level_length):
                    node = queue.pop()
                    level_arr.append(node.val)

                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

                res.append(level_arr)

            left_to_right = not left_to_right
        return res