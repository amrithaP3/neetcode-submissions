class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1 for n in nums]
        suff = [1 for n in nums]
        res = [1 for n in nums]

        # Build prefix array
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        # Build suffix array
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        
        # Build res (final array)
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]
        
        return res

        


        
