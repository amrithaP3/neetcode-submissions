class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict never raises a KeyError
        # the list indicates that the dict's values are lists
        mappings = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            mappings[tuple(count)].append(word)
        
        return mappings.values()

            

        