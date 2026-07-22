class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow=0
        # for i in range(len(nums)):
        #     if nums[i]!= val:
        #         nums[slow]=nums[i]
        #         slow+=1

        # return slow 

        slow=0
        fast=0

        while fast< len(nums):
            if nums[fast]!= val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1

        return slow

        