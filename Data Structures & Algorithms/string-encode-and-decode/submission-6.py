class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, s in enumerate(strs):
            encoded += str(len(s)) + "*" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            len_s = int(s[i:j])
            j += 1
            res.append(s[j:j+len_s])
            i = j + len_s

        return res