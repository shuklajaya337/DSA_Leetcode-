class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n= len(nums)
        st=[]
        nse=[n]*n
        pse=[-1]*n
        

        for i in range (n):
            while st and nums[st[-1]]>nums[i]:
                st.pop()
            if st:
                pse[i]=st[-1]

            st.append(i)

        st.clear()

        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()

            if st:
                nse[i]=st[-1]
            st.append(i)

        min_sum=0
        for i in range(n):
            left= i-pse[i]
            right =nse[i]-i

            min_sum+= nums[i]*left*right

       

        # Maximum 
        pse = [-1] * n
        nse = [n] * n
        st.clear()
        
        for i in range (n):
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            if st:
                pse[i]=st[-1]

            st.append(i)

        st.clear()

        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()

            if st:
                nse[i]=st[-1]
            st.append(i)

        max_sum=0
        for i in range(n):
            left= i-pse[i]
            right =nse[i]-i

            max_sum+= nums[i]*left*right

        
        return max_sum - min_sum

