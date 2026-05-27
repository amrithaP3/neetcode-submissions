class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # pivot is at last left pointer index
            nums[p], nums[r] = pivot, nums[p]

            if p > index:
                return quickSelect(l, p - 1)
            elif p < index:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
            
        return quickSelect(0, len(nums) - 1)
