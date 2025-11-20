# Problem: Longest Repeating Character Replacement (LeetCode 424)
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1) (Since the count dictionary will have at most 26 keys for uppercase English letters)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0 # Tracks the count of the most frequent char in the CURRENT window

        for r in range(len(s)):
            # Step 1: Add the current character s[r] to the count
            # (Hint: count[s[r]] = 1 + get old count)
            count[s[r]] = count.get(s[r],0)+1

            # Step 2: Update maxf
            # (Hint: Is the new count of s[r] bigger than the old maxf?)
            maxf = max(maxf, count[s[r]])

            # Step 3: The "Magic Formula"
            # Window Length = (r - l + 1)
            # If (Window Length - maxf) > k, the window is INVALID.
            if (r - l + 1) - maxf > k:
                # We must shrink the window from the left
                count[s[l]] -= 1
                l += 1
            
            # Step 4: Update the result with the current window size
            res = max(res, r - l + 1)
            
        return res

