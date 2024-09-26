"""
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {word: set(word) for word in strs}
        out = []
        group = []

        if not strs:
            print('empty input')
            return False

        for word in strs:
            if not group:
                group.append(word)
            else:
                for key, value in word_dict.items():
                    if word_dict.get(word) == value and key not in group:
                        group.append(key)
                out.append(group)
                group = []
        
        return out