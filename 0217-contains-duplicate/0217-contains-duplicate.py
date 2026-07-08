class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        dict={}

        for x in nums:
            if x in dict:
                dict[x]+=1
                return True
            else:
                dict[x]=1


        return False 
