class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        r,l=0,0
        maxS=0
        while r < len(s):
            while (s[r] in myset):
                myset.remove(s[l])
                l+=1
            myset.add(s[r])
            maxS = max(maxS,len(myset))
            r+=1
        return maxS