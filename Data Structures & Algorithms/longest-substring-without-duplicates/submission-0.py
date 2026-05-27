class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        maxLength = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[i])
            maxLength = max(maxLength, len(substring))

        return maxLength