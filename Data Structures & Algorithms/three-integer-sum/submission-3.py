class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            x = nums[i]

            if i > 0 and x == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                y = nums[j]
                z = nums[k]
                threeSum = x + y + z

                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    res.append([x, y, z])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        return res



        
