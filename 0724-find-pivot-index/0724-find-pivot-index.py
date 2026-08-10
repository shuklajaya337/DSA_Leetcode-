class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=0
        total=sum(arr)
        for i in range (n):
            prefix+=arr[i]
            ans = total - prefix
            if ans==prefix- arr[i]:
                return i 

        return -1

        
