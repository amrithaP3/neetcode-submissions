class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # combinations NOT permutations
        # time complexity: O(n*2^n)

        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # don't include nums[i]
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res
            
