class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        result = 0

        # returning min(maxLeft, maxRight)
        while l < r:
            # right pointer doesnt matter here bc left is bottleneck
            if leftMax < rightMax:
                l += 1
                amt = leftMax - height[l]
                result += amt if amt > 0 else 0
                leftMax = max(leftMax, height[l])
            # left ptr doesn't matter bc right is bottleneck
            else:
                r -= 1
                # this order also valid --> NO neg. checks
                # res only added to (pos amount) when height[r]
                # shorter than rightMax so if changed, res += 0
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result
