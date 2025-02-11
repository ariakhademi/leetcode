"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise. An anagram is a 
word or phrase formed by rearranging the letters of 
a different word or phrase, using all the original 
letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not s) or (not t):
            return False
        
        if len(s) != len(t):
            return False
        
        s_hash_map = {}
        t_hash_map = {}
        
        # assuming same length
        for i in range(len(s)):
            if s[i] not in s_hash_map:
                s_hash_map[s[i]] = 1
            else:
                s_hash_map[s[i]] += 1

            if t[i] not in t_hash_map:
                t_hash_map[t[i]] = 1
            else:
                t_hash_map[t[i]] += 1

        if s_hash_map == t_hash_map:
            return True
        else:
            return False