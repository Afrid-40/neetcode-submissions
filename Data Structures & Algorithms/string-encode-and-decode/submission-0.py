class Solution:

    def encode(self, strs: List[str]) -> str:
        re= []
        for s in strs:
            re.append(str(len(s)))
            re.append("#")
            re.append(s)
        return "".join(re)

    def decode(self, s: str) -> List[str]:
        re = []
        i =0
        while i <len(s):
            j = i
            while s[j] != '#':
                j += 1
            lenght = int(s[i:j])
            i =  j + 1
            j = i + lenght
            re.append(s[i:j])
            i = j 
        return re
