class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        i=0
        j=len(nums)-1
        mid=0

        while mid<= j:
            if nums[mid]==0:
                nums[i],nums[mid]= nums[mid],nums[i]
                i+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[j]=nums[j],nums[mid]
                j-=1
                


        