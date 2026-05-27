class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqDict = defaultdict(lambda: 0)
        count = [[] for i in range(len(nums) + 1)]
        print(count)

        for num in nums:
            freqDict[num] += 1
        
        for num in freqDict:
            count[freqDict[num]].append(num)

        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result

        # result = []
        # freqDict = defaultdict(lambda: 0)
        # tupList = []

        # for num in nums:
        #     freqDict[num] += 1
        
        # for num in freqDict:
        #     tupList.append((freqDict[num], num))
        
        # tupList.sort()

        # for i in range(len(tupList) - 1, -1, -1):
        #     if k > 0:
        #         result.append(tupList[i][1])
        #         k -= 1
        #     if k == 0:
        #         return result
             
        