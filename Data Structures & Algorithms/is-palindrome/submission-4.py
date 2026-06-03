class Solution:
    def isPalindrome(self, s: str) -> bool:
        alist = []
        for c in s:
            # isalnum() checks if a character is alphanumeric
            if c.isalnum():
                # need to append c.lower() to ensure case-insensitivity
                alist.append(c.lower())
        return alist == alist[::-1]
