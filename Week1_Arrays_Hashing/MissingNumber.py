# Problem: Missing Number
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxV = max(nums)


        for i in range(maxV):
            if i in nums:
                continue
            else:
                return i
        return maxV+1
    
# Problem: Missing Number
# Difficulty: Easy
# Time Complexity: O(N)
# Space Complexity: O(1)

# second way 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumE = (n*(n+1))//2

        sumA = sum(nums)

        return sumE-sumA