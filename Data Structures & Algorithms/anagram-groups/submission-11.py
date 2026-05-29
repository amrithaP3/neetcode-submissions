class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(lambda: [])

        for word in strs:
            charCount = [0] * 26
            for letter in word:
                charCount[ord(letter) - ord("a")] += 1
            
            tupVersion = tuple(charCount)
            mapping[tupVersion].append(word)
        
        out = list(mapping.values())

        return out