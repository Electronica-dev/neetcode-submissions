class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        # [-3, -3, 0, 1, 2, 3, 3]
        for i in range(len(nums) - 3):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:
                    continue
                
                l, r = j + 1, len(nums) - 1

                while l < r:
                    fourSum = x + y + nums[l] + nums[r]
                    if fourSum < target:
                        l += 1
                    elif fourSum > target:
                        r -= 1
                    else:
                        res.append([x, y, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        
        return res