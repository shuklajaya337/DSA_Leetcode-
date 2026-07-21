class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left=0
        right=n-1
        largest_product=n-1
        ans=[0]*n

        while left <= right:
            left_square= nums[left]*nums[left]
            right_square= nums[right]*nums[right]

            if left_square > right_square:
                ans[largest_product]=left_square
                left+=1
            else:
                ans[largest_product]= right_square
                right-=1


            largest_product-=1

        return ans 



