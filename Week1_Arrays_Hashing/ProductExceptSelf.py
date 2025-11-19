# Problem: Product of Array Except Self
# Difficulty: Medium
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [0] * n

        # 1. Build Left Products
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]

        # 2. Build Right Products (Go backwards)
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        # 3. Multiply them
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
            
        return result