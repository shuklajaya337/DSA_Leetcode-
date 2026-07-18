class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        next_element=0

        for i in range(n):
            if nums[i]!=0:
                nums[next_element],nums[i]=nums[i],nums[next_element]
                next_element+=1
                
            

