class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsLength = len(nums)

        # Time complexity of set() is O(n)
        numSet = set(nums)
        numSetLength = len(numSet)

        return True if numsLength > numSetLength else False