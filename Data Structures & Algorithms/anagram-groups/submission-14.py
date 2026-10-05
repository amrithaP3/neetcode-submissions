class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for key in strs:
            charMap = [0] * 26

            for char in key:
                charMap[ord(char) - ord("a")] += 1
            
            charTup = tuple(charMap)

            if charTup not in groups:
                groups[charTup] = [key]
            else:
                groups[charTup].append(key)
        
        return list(groups.values())

