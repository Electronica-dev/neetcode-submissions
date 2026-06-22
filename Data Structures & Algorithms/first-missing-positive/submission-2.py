class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if n == res:
                res = n + 1
        while res in nums:
            res += 1

        return res
        