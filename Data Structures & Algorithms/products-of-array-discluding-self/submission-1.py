class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 4, 6
        res = []
        l= 0

        while l < len(nums):
            temp = 1
            r = 0
            while r < len(nums):
                if l == r:
                    r += 1
                else:
                    temp *= nums[r]
                    r += 1
            l += 1
            res.append(temp)
        return res