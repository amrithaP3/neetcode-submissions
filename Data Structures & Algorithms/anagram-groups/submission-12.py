class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        adict = defaultdict(lambda: [])

        for word in strs:
            charCount = [0] * 26
            for i in range(len(word)):
                charCount[ord(word[i]) - ord("a")] += 1
            
            tupV = tuple(charCount)
            adict[tupV].append(word)
        
        return list(adict.values())