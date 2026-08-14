class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        running_sum=0
        prefix_sum=[0]*n

        for i in range(n):
            running_sum+=nums[i]
            prefix_sum[i] = running_sum

        return prefix_sum

        