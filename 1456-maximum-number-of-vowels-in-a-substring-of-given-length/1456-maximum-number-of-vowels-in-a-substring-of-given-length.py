class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        max_count=0
        count=0
        vowel={"a", "e", "i", "o", "u"}

        for j in range(len(s)):
            if s[j] in vowel:
                count+=1

            if j -i + 1 > k:
                if s[i] in vowel:
                    count-=1
                i+=1

            if j-i+1==k:
                max_count=max(max_count,count)

        return max_count