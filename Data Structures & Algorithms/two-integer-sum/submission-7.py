class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in numsmap:
                return [numsmap[diff], i]
            
            numsmap[val] = i