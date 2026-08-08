class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            n=len(arr)
            l=0
            count=0
            odd_count=0

            for r in range(n):
                if arr[r]%2!=0:
                    odd_count+=1

                while odd_count>k:
                    if arr[l] % 2 != 0:
                        odd_count-=1
                    l+=1

                count+= r-l+1

            return count

        return atmost(k)- atmost(k-1)

        