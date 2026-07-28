class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        n=len(arr)
        i=0
        freq={}
        ans=0

        for j in range (n):
            freq[arr[j]] = freq.get(arr[j], 0) + 1
            
            while len(freq) > 2:
                freq[arr[i]]-=1

                if freq[arr[i]]==0:
                    del freq[arr[i]]

                i+=1
            ans=max(ans,j-i+1)
        return ans 
        