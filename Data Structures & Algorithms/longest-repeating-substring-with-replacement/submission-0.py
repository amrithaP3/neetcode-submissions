class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(lambda: 0)
        result = 0

        l = 0
        for i in range(len(s)):
            count[s[i]] += 1
            
            # window length - # of most frequent chars
            # most freq chars = O(26) time bc at most 26 elements to look through
            # replacementNum = (i - l + 1) - max(count.values())
            while (i - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, i - l + 1)
        
        return result


