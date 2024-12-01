"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, current_combination):
            # base case
            if len(current_combination) == k:
                result.append(current_combination[:])
            # iterative case
            else:
                for number in range(start, n + 1):
                    current_combination.append(number)
                    backtrack(number + 1, current_combination)
                    current_combination.pop()

        backtrack(1, [])
        return result