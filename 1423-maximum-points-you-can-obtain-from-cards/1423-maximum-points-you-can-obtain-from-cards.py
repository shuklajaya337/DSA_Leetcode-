class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n=len(arr)
        l_sum=0
        r_sum=0
        max_sum=0
        

        for i in range (0,k):
            l_sum+=arr[i]
            max_sum=l_sum
        
        r_index=n-1
        for i in range (k-1,-1,-1):
            l_sum-=arr[i]
            r_sum+=arr[r_index]
            r_index-=1

            

            max_sum=max(max_sum,l_sum+r_sum)

        return max_sum
        