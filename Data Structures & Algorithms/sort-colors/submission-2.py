class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(arr, L, R, M):
            leftA, rightA = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            
            while j < len(leftA) and k < len(rightA):
                if leftA[j] < rightA[k]:
                    arr[i] = leftA[j]
                    j+=1
                else:
                    arr[i] = rightA[k]
                    k+=1
                i += 1
            
            while j < len(leftA):
                arr[i] = leftA[j]
                j += 1
                i += 1
            
            while k < len(rightA):
                arr[i] = rightA[k]
                k += 1
                i += 1
            
        
        def mergeSortArray(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSortArray(arr, l, m)
            mergeSortArray(arr, m + 1, r)
            mergeSort(arr, l, r, m)

        return mergeSortArray(nums, 0, len(nums) - 1)
