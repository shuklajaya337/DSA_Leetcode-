class Solution:
    def numSubarraysWithSum(self, arr: List[int], goal: int) -> int:
        n=len(arr)
        def atmost(goal):
            if goal<0:
                return 0

            l=0
            sum=0
            count=0

            for  r in range(n):
                sum+=arr[r]

                while sum> goal:
                    sum-=arr[l]
                    l+=1
                count+= r-l+1

            return count

        return atmost(goal)- atmost(goal-1)



        