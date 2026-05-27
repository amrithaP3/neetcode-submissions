class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLongest = 0

        for n in numSet:
            # identifies start of a sequence
            if (n - 1) not in numSet:
                longest = 1
                while(n + longest) in numSet:
                    longest += 1
                maxLongest = max(longest, maxLongest)
        return maxLongest

            