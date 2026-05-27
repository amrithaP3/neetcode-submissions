class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = []
        b = []
        for x in s:
            a.append(x)
        for y in t:
            b.append(y)
        
        a.sort()
        b.sort()

        if a == b:
            return True
        else:
            return False