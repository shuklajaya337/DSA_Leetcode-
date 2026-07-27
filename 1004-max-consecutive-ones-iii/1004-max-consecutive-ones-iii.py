class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        n=len(arr)
        i=0
        zero=0
        ans=0
        for j in range (n):
            if arr[j]==0:
                zero+=1

            while zero>k:
                if arr[i]==0:
                    zero-=1
                i+=1

            length=j-i+1
            ans=max(ans,length)

        return ans






        