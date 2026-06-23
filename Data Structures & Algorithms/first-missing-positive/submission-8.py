class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            curr_num = abs(nums[i])
            if curr_num <= len(nums) and curr_num - 1 >= 0:
                if nums[curr_num-1] == 0:
                    nums[curr_num-1] = -(len(nums) + 1)
                elif nums[curr_num - 1] > 0:
                    nums[curr_num-1] *= -1
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
