class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        symbols = {  ")":"(","]":"[" , "}":"{" }
        for ch in s:
            if ch in symbols:
                if st and st[-1] == symbols[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return True if not st else False

