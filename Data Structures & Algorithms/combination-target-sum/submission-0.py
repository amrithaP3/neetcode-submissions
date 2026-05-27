class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # want combinations NOT permutations!
        # time complexity of O(2^t)

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # CAN include candidate - first branch of decision tree
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            # CAN'T include candidate - second branch of decision tree
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res



