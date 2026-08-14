class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq = {0: 1}

        prefix = 0
        count = 0

        for i in range(n):
            prefix += nums[i]
            needed= prefix -k  # previous prefix sum= needed 

            if needed in freq:
                count += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count
        