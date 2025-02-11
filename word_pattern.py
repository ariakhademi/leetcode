"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # comma separated
        s_words = s.split()

        if len(pattern) != len(s_words):
            return False
        
        # pattern -> s_words
        hash_map1 = {}
        # s_words -> pattern
        hash_map2 = {}
        # assuming s and pattern have same length
        for i in range(len(s_words)):
            if (pattern[i] not in hash_map1) and (s_words[i] not in hash_map2):
                hash_map1[pattern[i]] = s_words[i]
                hash_map2[s_words[i]] = pattern[i]
            else:
                if pattern[i] != hash_map2.get(s_words[i]):
                    return False
        return True
        
