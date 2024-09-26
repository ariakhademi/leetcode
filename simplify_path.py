"""
You are given an absolute path for a Unix-style file system, 
which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above 
should be treated as a valid directory or file name. 
For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or 
double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # fill the stack with the valid string
        stack = []
        partitions = path.split('/')

        for part in partitions:
            if part == '.' or part == '':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(part)

        simplified_str ='/' + '/'.join(part for part in stack)

        return simplified_str