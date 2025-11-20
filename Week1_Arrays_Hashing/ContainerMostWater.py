# Problem: Container With Most Water (LeetCode 11)
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start Pointers at the EDGES
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            # Calculate area for current window
            area = (r-l) * min(height[r],height[l])
            # Check which wall is shorter?
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1
            res = max(res,area)
            # Update res
            # Move the pointer of the SHORTER wall inward
            
            
        return res