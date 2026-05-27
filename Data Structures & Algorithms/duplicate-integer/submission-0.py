class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            start = i + 1
            for x in range(start, len(nums)):
                if nums[i] == nums[x]:
                    return True
        return False
                