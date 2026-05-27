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
            
            # Using tuples since they are IMMUTABLE!
            tupVersion = tuple(charCount)
            if tupVersion in mapping:
                mapping[tupVersion].append(word)
            else:
                mapping[tupVersion] = [word]
        
        # .values() returns a dict view object so need to convert it to a list!
        return list(mapping.values())
            


