class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        count=0
        ans=0

        for num in range(len(arr)):
            if arr[num]==1:
                count+=1
                ans=max(ans,count)
            else:
                count=0

        return ans 
        