class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(lambda: 0)
        tDict = defaultdict(lambda: 0)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sDict[s[i]] += 1
            tDict[t[i]] += 1
        
        return (sDict == tDict)