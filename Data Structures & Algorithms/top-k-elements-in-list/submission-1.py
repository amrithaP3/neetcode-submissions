class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqDict = defaultdict(lambda: 0)
        tupList = []

        for num in nums:
            freqDict[num] += 1
        
        for num in freqDict:
            tupList.append((freqDict[num], num))
        
        tupList.sort()

        for i in range(len(tupList) - 1, -1, -1):
            if k > 0:
                result.append(tupList[i][1])
                k -= 1
            if k == 0:
                return result


        # freqArr = [[]] * len(nums)
        # count = defaultdict(int)
        # result = []
    
        # for n in nums:
        #     count[n] += 1

        # print(count)
        # for n, freq in count.items():
        #     freqArr[freq].append(n)
        #     print(freqArr)
        
        # print(freqArr)
        # for a in freqArr[-1::]:
        #     for b in a:
        #         if k > 0:
        #             result.append(b)
        #             k -= 1
        #         else:
        #             return result

            

        '''
        for n, freq in count.items():
            sort.append((freq, n))
        
        sort.sort()
        for freq, n in sort[::-1]:
            if k > 0:
                result.append(n)
                k -= 1
            else:
                break
        
        return result
        '''

        


        #return hey


        '''
        output = []
        minFreq = 1
        freq = 1
        subj = nums[0]

        for num in nums[1:]:
            if num == subj:
                freq += 1
            else:
                freq = 1
                subj = num
                continue
            if freq > minFreq and k > 0:
                output = [num]
                minFreq = freq
                freq = 1
                subj = num
                k -= 1
            elif freq == minFreq:
                output.append(num)
        
        return output
        '''
             
        