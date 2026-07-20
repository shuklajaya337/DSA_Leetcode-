class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        max_water=0


        while left< right :


            width=right-left
            heights=min(height[right],height[left])

            water=width*heights

            max_water=max(water,max_water)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1


        return max_water 


        