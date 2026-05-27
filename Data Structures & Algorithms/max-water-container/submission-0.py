class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0

        for i in range(len(heights)):
            l = 0
            r = len(heights) - 1

            while l < r:
                smallest = min(heights[l], heights[r])
                potentialMax = (r - l) * smallest
                if potentialMax > currMax:
                    currMax = potentialMax
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        
        return currMax

                