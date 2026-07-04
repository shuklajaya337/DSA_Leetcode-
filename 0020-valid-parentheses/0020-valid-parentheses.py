class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            if ch in "({[":
                st.append(ch)

            else:
                if not st:
                    return False

                if st[-1] != pairs[ch]:
                    return False

                st.pop()

        return len(st) == 0
        