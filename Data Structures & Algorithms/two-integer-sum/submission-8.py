class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}

        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in candidates:
                return [candidates[candidate], i]
            else:
                candidates[nums[i]] = i
            