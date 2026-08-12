class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=0
        freq={}
        max_length=0

        for r in range (n):
            freq[nums[r]]=freq.get(nums[r],0)+1

            while freq[nums[r]] > k:
                freq[nums[l]]-=1
                l+=1
            
            length=r-l+1
            max_length=max(max_length, length)

        return max_length    

        