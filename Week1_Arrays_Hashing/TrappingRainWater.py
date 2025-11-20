# Problem: Trapping Rain Water (LeetCode 42)
# Difficulty: Hard
# Time Complexity: O(n)
# Space Complexity: O(n) (Due to max_left and max_right arrays)
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [] 
        max_right = [0] * len(height)
        i = 1
        max_left.append(height[0])
        while i < len(height):
            if height[i]> max_left[i-1]:
                max_left.append(height[i])
            else:
                max_left.append(max_left[i-1])
            i+=1
        i = len(height)-2
        k = len(height)-1
        max_right[k] = height[k]

        while i >= 0:
            if height[i]> max_right[i+1]:
                max_right[i]= height[i]
            else:
                max_right[i]= max_right[i+1]
            i-=1
        i = 0
        res = 0
        while i < len(height)-1:
            res += min(max_left[i], max_right[i]) - height[i]
            i+=1
        return res

