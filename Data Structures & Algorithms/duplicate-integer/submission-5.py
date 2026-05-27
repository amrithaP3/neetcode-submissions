class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsLength = len(nums)

        numSet = set(nums)
        numSetLength = len(numSet)

        return True if numsLength > numSetLength else False