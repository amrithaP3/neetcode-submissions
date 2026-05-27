class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i == 0 or nums[i] != nums[i -1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    add = val + nums[l] + nums[r]
                    if add > 0:
                        r -= 1
                    elif add < 0:
                        l += 1
                    else:
                        res.append([val, nums[l], nums[r]])

                        # keep checking but not if same element!
                        # keep moving left pointer if same element
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        
        return res
