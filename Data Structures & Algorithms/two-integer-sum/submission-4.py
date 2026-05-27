class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            start = i + 1
            for j in range(start, len(nums)):
                if (nums[i] + nums[j]) == target:
                    print(nums[i] + nums[j])
                    result.append(i)
                    result.append(j)
                    return result
                
        