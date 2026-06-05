class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        freqDict = defaultdict(lambda: 0)

        for n in nums:
            freqDict[n] += 1
        
        maxFreq = max(freqDict.values()) + 1

        # freqList = [[]] * maxFreq WILL NOT WORK 
        # because change to one sublist results in same change to all other sublists
        freqList = [[] for i in range(maxFreq)]
        for num in freqDict:
            freq = freqDict[num]
            freqList[freq].append(num)

        required = k
        for i in range(len(freqList) - 1, -1, -1):
            for item in freqList[i]:
                out.append(item)
                required -= 1

                if required == 0:
                    return out