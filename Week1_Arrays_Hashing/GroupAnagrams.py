# Problem: Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Time Complexity: O(N * K log K) where N is the number of strings and K is the maximum length of a string
# Space Complexity: O(N * K)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myresult = {}  # Standard dictionary

        for word in strs:
            # 1. Create the Key (sort the letters)
            sorted_chars = sorted(word)
            key = "".join(sorted_chars) 
            
            # 2. Check if key exists
            if key in myresult:
                # If key exists, append this word to the existing list
                myresult[key].append(word)
            else:
                # If key is NEW, create a NEW list with this word inside
                myresult[key] = [word]
        
        # 3. The result demands a List of Lists. 
        # myresult currently looks like: {'aet': ['eat', 'tea'], 'ant': ['tan']}
        # .values() extracts just the lists: [['eat', 'tea'], ['tan']]
        return list(myresult.values())