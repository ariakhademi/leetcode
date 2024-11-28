"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        my_dictionary = {
            '2':'abc',
            '3':'def',
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        if not digits:
            return []

        result = []

        def backtrack(idx, current_combination):
            # base case
            if idx == len(digits):
                result.append(current_combination)

            # iterative case
            else:
                current_digit = digits[idx]
                current_letters = my_dictionary.get(current_digit)
                for letter in current_letters:
                    backtrack(idx + 1, current_combination + letter)

        backtrack(0,"")

        return result