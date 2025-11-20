# Problem: 3Sum (LeetCode 15)
# Difficulty: Medium  
# Time Complexity: O(n^2)
# Space Complexity: O(n) (Due to sorting and result storage)

from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sorting is crucial: O(N log N)

        for k, num in enumerate(nums):
            # 1. Skip duplicates for the 'pivot' number (k)
            # We check k > 0 to ensure we don't check index -1
            if k > 0 and num == nums[k - 1]:
                continue

            # Setup Two Pointers for the REMAINING part of the array
            l, r = k + 1, len(nums) - 1
            
            while l < r:
                threeSum = num + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Found a match!
                    res.append([num, nums[l], nums[r]])
                    
                    # Move pointers logic
                    l += 1
                    # r -= 1 # Optional, the loop will handle it naturally, but faster to move both
                    
                    # 2. Skip duplicates for the 'left' pointer
                    # While we are not crossing and the value is same as previous, keep moving
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res