class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, th: int) -> int:
        n=len(arr)
        i=0
        j=k-1
        count=0
        sum=0

        for a in range(k):
            sum+=arr[a]
        avg=sum/k
        if avg>=th:
            count+=1
        
        while j<n:
            j+=1
            if j==n:
                break
            sum=sum-arr[i]+arr[j]
            avg=sum/k
            i+=1
            
            if avg>=th:
                count+=1
            

        return count




        