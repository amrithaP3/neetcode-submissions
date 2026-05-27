class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Q: How would we determine anagrams in the first place? 
        # A: comparing counts of characters

        # Group anagrams using those counts!
        mapping = {}

        for word in strs:
            charCount = [0] * 26
            for i in range(len(word)):
                charCount[ord(word[i]) - ord("a")] += 1
            
            tupVersion = tuple(charCount)
            if tupVersion in mapping:
                mapping[tupVersion].append(word)
            else:
                mapping[tupVersion] = [word]
        
        return list(mapping.values())
            


