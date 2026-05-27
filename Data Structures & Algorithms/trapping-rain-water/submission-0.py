class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        result = 0

        while l < r:
            # right pointer doesnt matter here bc left is bottleneck
            if leftMax < rightMax:
                l += 1
                amt = leftMax - height[l]
                result += amt if amt > 0 else 0
                leftMax = max(leftMax, height[l])
                
            else:
                r -= 1
                amt = rightMax - height[r]
                result += amt if amt > 0 else 0
                rightMax = max(rightMax, height[r])
        
        return result
