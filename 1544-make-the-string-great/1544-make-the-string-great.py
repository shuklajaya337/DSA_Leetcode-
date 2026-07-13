class Solution:
    def makeGood(self, s: str) -> str:

        st = []

        for ch in s:

            if len(st) > 0:

                ch1 = st[-1]  
                ch2 = ch       

                if ch1.lower() == ch2.lower() and ch1 != ch2:
                    st.pop()
                else:
                    st.append(ch2)

            else:
                st.append(ch)

        return "".join(st)
        