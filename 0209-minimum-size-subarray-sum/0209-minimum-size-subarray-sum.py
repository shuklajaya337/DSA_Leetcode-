class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        res = float('inf')
        sum=0
        while j<n:
            sum+=nums[j]
            while sum>=target:
                length=j-i+1
                res=min(res,length)
                sum-=nums[i]
                i+=1
            j+=1

        if res == float('inf'):
            return 0
        else:
            return res


        