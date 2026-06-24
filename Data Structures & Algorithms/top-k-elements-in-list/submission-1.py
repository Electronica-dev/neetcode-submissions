class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 0
        
        buckets = [[] for _ in range(len(nums))]
        for ke, v in hmap.items():
            buckets[v].append(ke)
        print(buckets)
        res = []
        
        for i in range(len(buckets) - 1, -1, -1):
            for ele in buckets[i]:

                while k > 0 and buckets[i]:
                    res.append(buckets[i].pop())
                    k -= 1
        return res