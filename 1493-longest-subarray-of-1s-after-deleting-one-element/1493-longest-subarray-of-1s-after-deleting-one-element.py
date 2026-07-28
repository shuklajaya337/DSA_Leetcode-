class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        i=0
        res=0
        zero=0

        for j in range(len(arr)):
            if arr[j]==0:
                zero+=1
                while zero > 1:
                    if arr[i]==0:
                        zero-=1
                    i+=1

            res=max(res,j-i)

        return res 

         