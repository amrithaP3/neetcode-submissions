class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        sort = []
    
        for n in nums:
            count[n] += 1
        
        for n, freq in count.items():
            sort.append((freq, n))
        
        sort.sort()
        print(sort)
        for freq, n in sort[::-1]:
            if k > 0:
                result.append(n)
                k -= 1
            else:
                break
        
        return result


        


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
             
        