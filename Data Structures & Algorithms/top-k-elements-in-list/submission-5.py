class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        freqDict = defaultdict(lambda: 0)

        for n in nums:
            freqDict[n] += 1
        
        maxFreq = max(freqDict.values()) + 1

        freqList = [[] for a in range(maxFreq)]

        for key in freqDict:
            freq = freqDict[key]

            freqList[freq].append(key)
        
        required = k
        for i in range(len(freqList) - 1, -1, -1):
            for x in freqList[i]:
                if required > 0:
                    res.append(x)
                    required -= 1
        
        return res