# Problem: Top K Frequent Elements
# Difficulty: Medium
# Time Complexity: O(N log N)
# Space Complexity: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # list(count.items()) -> [(1,3), (2,2), (3,1)]
        # key=lambda x: x[1] -> tells sort to look at the COUNT (index 1), not the number
        # reverse=True -> Biggest counts first
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Now sorted_items is [(1,3), (2,2), (3,1)]
        # We just need the numbers (index 0), and we need the first k of them
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
            
        return result