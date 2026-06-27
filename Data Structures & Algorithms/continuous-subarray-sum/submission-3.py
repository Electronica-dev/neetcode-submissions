class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        hmap[0] = -1
        curr = 0
        for i, n in enumerate(nums):
            curr += n
            rem = curr % k
            if rem in hmap and i - hmap[rem] >= 2:
                return True
            if rem not in hmap:
                hmap[rem] = i
        
        return False