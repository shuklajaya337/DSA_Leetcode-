class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        freq={0:1}
        prefix=0
        for i in range(n):
            prefix+=nums[i]
            remainder = prefix % k

            if remainder<0:
                remainder+=k

            if remainder in freq:
                count+=freq[remainder]

            freq[remainder]=freq.get(remainder,0)+1

        return count

        