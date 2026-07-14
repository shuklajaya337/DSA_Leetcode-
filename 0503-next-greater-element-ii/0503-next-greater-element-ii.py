class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [0] * n      
        stack = []

        for num in range(2 * n - 1, -1, -1):

            while stack and stack[-1] <= nums[num % n]:
                stack.pop()

            if num < n:
                if stack:
                    nge[num] = stack[-1]
                else:
                    nge[num] = -1

            stack.append(nums[num % n])

        return nge
        