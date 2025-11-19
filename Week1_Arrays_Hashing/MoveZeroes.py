# Problem: Move Zeroes
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        # r (the scout) checks every index automatically
        for r in range(len(nums)):
            if nums[r] != 0:
                # Found a non-zero! Swap it into the 'l' position
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 # Move 'l' forward to accept the next non-zero