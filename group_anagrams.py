"""
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dictionary = {}

        if not strs:
            return [0]

        # key idea is sorting
        for word in strs:
            sorted_word = ''.join(sorted(word))
            print(sorted_word)
            if sorted_word not in my_dictionary:
                my_dictionary[sorted_word] = [word]
            else:
                my_dictionary[sorted_word].append(word)

        return list(my_dictionary.values())