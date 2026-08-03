class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        n=len(arr)
        i=0
        zero=0
        ans=0
        for j in range (n):
            if arr[j]==0:
                zero+=1

            if  zero>k:
                if arr[i]==0:
                    zero-=1
                i+=1
            
            
            ans=max(ans,j-i+1)

        return ans






        