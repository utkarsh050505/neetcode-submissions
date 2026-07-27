class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "_" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Read the length
            while s[j] != "_":
                j += 1

            length = int(s[i:j])

            # Read the string
            res.append(s[j + 1 : j + 1 + length])

            # Move to the next encoded string
            i = j + 1 + length

        return res