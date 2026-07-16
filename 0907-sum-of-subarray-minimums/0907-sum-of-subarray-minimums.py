class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n= len(arr)
        st=[]
        nse=[n]*n
        pse=[-1]*n
        mod=10**9+7
        ans=0

        for i in range (n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                pse[i]=st[-1]

            st.append(i)

        st.clear()

        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()

            if st:
                nse[i]=st[-1]
            st.append(i)

        
        for i in range(n):
            left= i-pse[i]
            right =nse[i]-i

            ans=(ans+ arr[i]*left*right)% mod

        return ans

