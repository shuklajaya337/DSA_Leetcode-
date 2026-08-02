class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n==0:
            return True
        x=n
        rev=0
        while n>0:
            digit=n%10
            rev=rev*10+digit
            n=n//10

            if x==rev:
                return True
        return False


        