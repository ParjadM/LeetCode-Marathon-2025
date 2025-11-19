# Problem: Single Number
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myset = set()

        for num in nums:
            if num in myset:
                myset.remove(num)
            else:
                myset.add(num)
        return list(myset)[0]