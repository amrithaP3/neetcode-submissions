class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s2 = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                s1 += s[i]
        
        for i in range(len(s) -1, -1, -1):
            if s[i].isalpha() or s[i].isdigit():
                s2 += s[i]

        return s1.lower() == s2.lower()
             