class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        ans=0
        max_freq=0
        freq={}
        for j in range(len(s)):
            freq[s[j]]=freq.get(s[j],0)+1
            max_freq=max(freq.values())
            win_len=j-i+1
            change= win_len-max_freq

            while change >k:
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
                win_len=j-i+1
                change= win_len-max_freq
            ans=max(ans,win_len)

        return ans
                



        