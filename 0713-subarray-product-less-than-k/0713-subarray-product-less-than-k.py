class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        if k<=1:
            return 0
        n=len(arr)
        i=0
        j=0
        product=1
        count=0
        while j<n:
            product*=arr[j]
            while product >= k:
                product //=arr[i]
                i+=1
            count=count+(j-i+1)
            j+=1

        return count 
        

        