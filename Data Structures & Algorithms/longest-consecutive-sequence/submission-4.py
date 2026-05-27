class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLongest = 0

        for n in numSet:
            # identifies start of a sequence
            # doesn't have a left neighbor means start of sequence
            if (n - 1) not in numSet:
                longest = 1

                # adding longest to n while inc. longest allows
                # us to check consecutive while making n remain the same
                while(n + longest) in numSet:
                    longest += 1
                
                # typical changing max when it has changed
                maxLongest = max(longest, maxLongest)
        return maxLongest

            