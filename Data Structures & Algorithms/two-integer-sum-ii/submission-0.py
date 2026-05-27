class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            diff = target - numbers[i]

            left = i
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] > diff:
                    right = mid - 1
                else:
                    left = mid + 1
        
        
        
        
        
        
        
