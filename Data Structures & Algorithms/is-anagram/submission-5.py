class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(t) < len(s):
            return False
        
        sDict, tDict = {}, {}

        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
            
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        
        print(sDict)
        print(tDict)
        return True if sDict == tDict else False
        