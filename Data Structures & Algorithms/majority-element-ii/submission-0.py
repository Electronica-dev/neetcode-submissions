class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = len(nums) // 3
        res = []
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 0
        
        for k, v in hmap.items():
            if v >= occ:
                res.append(k)
        
        return res