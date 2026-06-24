class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 0
        
        res = []
        for ke, v in hmap.items():
            res.append((ke, v))
        
        res.sort(key=lambda x: x[1], reverse=True)
        top = res[0:k]
        
        res = []
        for t in top:
            res.append(t[0])
        
        return res