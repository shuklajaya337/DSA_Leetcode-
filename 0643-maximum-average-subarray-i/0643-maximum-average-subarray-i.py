class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        n=len(arr)
        i=0
        j=k-1
        res = float('-inf')
        sum=0

        for l in range (k):
            sum+=arr[l]
        avg= sum/k
        while j<n:
            res=max(res,avg)
            j+=1
            if j==n:
                break
            
            sum = sum - arr[i]+arr[j]
            i+=1
            avg=sum/k
                
        return res 

                


        