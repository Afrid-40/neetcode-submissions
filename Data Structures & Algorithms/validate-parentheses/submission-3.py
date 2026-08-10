class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {"(": ")", "{": "}", "[": "]"}

        for i in s:
            if i in d:
                st.append(i)
            else:
                if not st:
                    return False

                if d[st[-1]] != i:
                    return False

                st.pop()

        return not st