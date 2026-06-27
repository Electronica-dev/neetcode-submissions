class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        i = 0
        s = 0
        res = 0
        while i < len(nums):
            s += nums[i]
            if s - k in hmap:
                res += hmap[s-k]
            hmap[s] += 1
            i += 1

        return res