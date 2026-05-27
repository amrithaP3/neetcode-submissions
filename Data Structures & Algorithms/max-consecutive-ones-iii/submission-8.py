class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l = 0
        unused = k

        for r in range(len(nums)):
            unused -= (1 if nums[r] == 0 else 0)
            
            while unused < 0:
                unused += (1 if nums[l] == 0 else 0)
                l += 1
            
            maxLen = max(maxLen, r - l + 1)

        return maxLen


            
