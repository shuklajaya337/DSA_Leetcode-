class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        n=len(arr)
        left=0
        total = sum(arr)
        for i in range(n):
            right= sum(arr)-left-arr[i]

            if left==right:
                return i
            left+=arr[i]
        return -1

        
