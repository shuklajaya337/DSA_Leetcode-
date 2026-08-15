class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.prefix=[0]*n

        if n>0:
            self.prefix[0]=nums[0]

        for i in range(1,n): 
            self.prefix[i] = self.prefix[i-1] + nums[i]


    
    def sumRange(self, l: int, r: int) -> int:
        if l==0:
           return self.prefix[r]

        return self.prefix[r]-self.prefix[l-1]

        
 