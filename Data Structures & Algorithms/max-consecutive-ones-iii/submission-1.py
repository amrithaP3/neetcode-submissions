class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        unused = k

        l, r = 0, 0
        currWindowLen = 0

        while r < len(nums):
            if nums[r] == 1:
                currWindowLen += 1
                r += 1
            elif unused > 0 and nums[r] != 1:
                currWindowLen += 1
                unused -= 1
                r += 1
            elif unused == 0 and nums[r] == 0:
                maxLen = max(maxLen, currWindowLen)
                currWindowLen = 0
                
                l += 1
                r = l
                unused = k
        
        return max(maxLen, currWindowLen)



            
