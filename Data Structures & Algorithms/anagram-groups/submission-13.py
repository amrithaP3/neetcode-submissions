class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aDict = defaultdict(lambda: [])

        for word in strs:
            charCount = [0] * 26
            for i in range(len(word)):
                charCount[ord(word[i]) - ord("a")] += 1
            
            tupVersion = tuple(charCount)
            aDict[tupVersion].append(word)
        
        return list(aDict.values())