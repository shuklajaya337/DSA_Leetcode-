class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]

        for ch in s:
            if ch!="#":
                st1.append(ch)
            elif len(st1)>0:
                st1.pop()
            else: 
                pass
     
        for ch in t:
            if ch!="#":
                st2.append(ch)
            elif len(st2)>0:
                st2.pop()
            else: 
                pass

        if st1 == st2:
            return True
        else:
            return False
        