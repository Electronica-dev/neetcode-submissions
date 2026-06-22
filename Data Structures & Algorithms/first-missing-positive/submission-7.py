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
                else:
                    nums[curr_num-1] = -abs(nums[curr_num-1])
        
        print(nums)
        res = 1
        for j in range(len(nums)):
            if nums[j] < 0:
                res = j + 2
            else:
                break
        
        return res
