class Solution:
    def decodeString(self, s: str) -> str:
        def parse_num(i):
            q = i
            while s[q].isnumeric():
                q += 1
            return int(s[i:q]), q-i
        def _decodeString(i) -> (str, int):
            if i >= len(s):
                return "", 0
            elif s[i].isnumeric():
                cnt, off = parse_num(i)
                out, off2 = _decodeString(i+off)
                out2, off3 = _decodeString(i+off+off2)
                return cnt*out + out2, off+off2+off3
            elif s[i].isalpha():
                out, off = _decodeString(i+1)
                return s[i]+out, off+1
            elif s[i] == "[":
                out, off = _decodeString(i+1)
                return out, off+1
            elif s[i] == "]":
                return "", 1
        return _decodeString(0)[0]

