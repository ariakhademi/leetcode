"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the
input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_dict = {')':'(', '}':'{', ']':'['}

        stack = []

        # iterating and pushing to stack
        for char in s:
            if stack and stack[-1] == char_dict.get(char):
                stack.pop()
            else:
                stack.append(char)
        
        # if stack is empty, string is valid
        if not stack:
            return True
        else:
            return False