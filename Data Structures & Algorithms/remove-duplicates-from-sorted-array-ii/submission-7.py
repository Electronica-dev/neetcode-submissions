class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,0
        while j < len(nums):
            print(nums, i, j,nums[i], nums[j])
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j - i >= 2:
                nums[i:j] = [nums[i]] * 2
                i = j - 1
            else:
                i = j

        return len(nums)        