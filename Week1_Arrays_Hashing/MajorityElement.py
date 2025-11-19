# Problem: Majority Element
# Difficulty: Easy
# Time Complexity: O(N log N)
# Space Complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
# Problem: Majority Element
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(N)    
# my answer 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myhash = {}

        for num in nums:
            myhash[num] = myhash.get(num,0)+1

        return max(myhash, key=myhash.get)