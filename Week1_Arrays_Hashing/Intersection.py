# Problem: Intersection of Two Arrays
# Difficulty: Easy
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        # This finds the intersection instantly (O(N+M))
        # Iterate through the smaller set for speed
        return list(set1.intersection(set2)) 
        # OR manually: [x for x in set1 if x in set2]