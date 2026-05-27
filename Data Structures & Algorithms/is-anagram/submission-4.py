class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This is the dictionary version - O(n)
        if len(s) != len(t):
            return False
        
        a, b = {}, {}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] += 1
            else:
               a[s[i]] = 1 
            if t[i] in b:
                b[t[i]] += 1
            else:
               b[t[i]] = 1
        
        if a == b:
            return True
        else:
            return False