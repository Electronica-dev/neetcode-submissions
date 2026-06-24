class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        maxH = height[0]

        for i in range(len(height)):
            maxLeft.append(maxH)
            maxH = max(maxH, height[i])
        
        maxH = 0
        for i in range(len(height) - 1, -1, -1):
            print(i, maxH)
            maxRight.append(maxH)
            maxH = max(maxH, height[i])
        
        maxRight = list(reversed(maxRight))
        
        res = 0
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                res += water
        
        return res