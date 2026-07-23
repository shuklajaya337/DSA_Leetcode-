class Solution:
    def sortArrayByParityII(self, arr: List[int]) -> List[int]:
        n = len(arr)

        i = 0     
        j = 1     

        while i < n and j < n:

            if arr[i] % 2 == 0:
                i += 2

            elif arr[j] % 2 == 1:
                j += 2

            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 2
                j += 2

        return arr
        
                
        