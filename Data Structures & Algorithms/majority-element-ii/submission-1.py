class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1
            
            if len(hmap) > 2:
                for k, v in hmap.items():
                    if v > 1:
                        hmap[k] -= 1
        
        res = []
        for num in hmap:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
    
        return res
            