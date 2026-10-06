class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        APPROACH: prefix sums + hashmap counting
        count = {prefix sum: number of subarrays that can sum to k}
        prefix[i - 1] = prefix[j] - k
        '''
        total = 0
        count = {0: 1}
        prev_sum = 0

        for n in nums:
            curr_sum = n + prev_sum
            candidate_sum = curr_sum - k
            
            if candidate_sum in count:
                total += count[candidate_sum]
            
            count[curr_sum] = count.get(curr_sum, 0) + 1
            prev_sum = curr_sum
        
        return total
        

