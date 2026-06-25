class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            tmp = 1
            for j, m in enumerate(nums):
                if i == j:
                    continue
                else:
                    tmp *= m
            res.append(tmp)
        
        return res