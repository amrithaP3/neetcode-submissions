class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use bucketsort!!
        out = []

        # Collect frequencies in a dict!
        freqDict = defaultdict(lambda: 0)

        for num in nums:
            freqDict[num] += 1
        
        # Create a list where indices correspond to frequency
        maxFreq = max(freqDict.values()) + 1
        freqList = [[] for i in range(maxFreq)]

        for key in freqDict:
            freq = freqDict[key]
            freqList[freq].append(key)

        left = k
        for i in range(len(freqList) - 1, -1, -1):
            for x in range(len(freqList[i])):
                if left > 0:
                    out.append(freqList[i][x])
                    left -= 1
                
                if left == 0:
                    return out

