class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                x = nums[i]
                y = nums[j]
                if x + y == target:
                    return [i, j]
                else:
                    j += 1
        