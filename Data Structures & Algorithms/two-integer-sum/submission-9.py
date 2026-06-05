class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        out = []

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in diffMap:
                out = [diffMap[diff], i]
                return out
            else:
                diffMap[nums[i]] = i