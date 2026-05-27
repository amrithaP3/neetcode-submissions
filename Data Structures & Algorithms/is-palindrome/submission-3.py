class Solution:
    def isPalindrome(self, s: str) -> bool:
        alist = []
        for c in s:
            if c.isalnum():
                alist.append(c.lower())
        return alist == alist[::-1]
