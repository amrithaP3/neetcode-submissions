class Solution:
    def isPalindrome(self, s: str) -> bool:
        pList = []

        for c in s:
            if c.isalnum():
                pList.append(c.lower())
        
        if pList == pList[::-1]:
            return True
        else:
            return False