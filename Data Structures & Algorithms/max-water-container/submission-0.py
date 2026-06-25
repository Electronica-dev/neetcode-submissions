class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            leftH = heights[l]
            rightH = heights[r]
            area = min(leftH, rightH) * (r - l)
            maxWater = max(maxWater, area)
            if leftH <= rightH:
                l += 1
            else:
                r -= 1
        
        return maxWater
