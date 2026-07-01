from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low , high = 1, max(nums)
        while (low<= high):
            mid=(low+high)//2

            sum=0
            for num in nums :
                sum += ceil(num/mid)
            if ( sum<= threshold):
                high=mid-1
            else:
                low=mid+1

        return low

        