# Problem: Best Time to Buy and Sell Stock (LeetCode 121)
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left=Buy, Right=Sell
        maxP = 0

        while r < len(prices):
            # is this a profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # We found a price LOWER than our current buy price.
                # Make this the new buy price immediately.
                l = r 
            
            r += 1 # Always move the right pointer forward to look for future sales
            
        return maxP