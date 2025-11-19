# Problem: Valid Anagram
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        myresult = {}


        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        for char in t:
            myresult[char] = myresult.get(char,0)+1
        return hashmap == myresult