# Problem: Two Sum
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash = {}

        for i,num in enumerate(nums):
            res = target - num
            if (res in myhash):
                return (i,myhash[res])
            else:
                myhash[num] = i

        return -1