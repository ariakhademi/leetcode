"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_sb = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                # see if s[i:j] has any repetitive chars
                visited = []
                repetitive = False
                for char in s[i:j]:
                    if char in visited:
                        repetitive = True
                        break
                    else:
                        visited.append(char)
                if repetitive == False and len(s[i:j]) > len(longest_sb):
                    longest_sb = s[i:j]
        return len(longest_sb)