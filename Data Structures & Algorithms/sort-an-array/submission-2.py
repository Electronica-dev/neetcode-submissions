class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, L, M, R):
            left, right = arr[L:M + 1], arr[M + 1:R + 1]
            ar_p, le_sub_p, ri_sub_p = L, 0, 0

            while le_sub_p < len(left) and ri_sub_p < len(right):
                if left[le_sub_p] <= right[ri_sub_p]:
                    arr[ar_p] = left[le_sub_p]
                    le_sub_p += 1
                else:
                    arr[ar_p] = right[ri_sub_p]
                    ri_sub_p += 1
                ar_p += 1
            
            while ri_sub_p < len(right):
                arr[ar_p] = right[ri_sub_p]
                ri_sub_p += 1
                ar_p += 1            
            while le_sub_p < len(left):
                arr[ar_p] = left[le_sub_p]
                le_sub_p += 1
                ar_p += 1



        def mergeSortArray(arr, l, r):
            if l >= r:
                return
            
            m = (l + r) // 2
            mergeSortArray(nums, l, m) # left
            mergeSortArray(nums, m + 1, r) # right
            mergeSort(arr, l, m, r) # in place
        
        mergeSortArray(nums, 0, len(nums) - 1)
        return nums
