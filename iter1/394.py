# k[abc]....
# abcd3[abcd]fff
# [abc] x not a valid string

class Solution:
    def decodeKString(self, s: str) -> str:
        l = s.find("[")
        cnt = int(s[:l])
        return ''.join([self.decodeString(s[l+1:-1]) for _ in cnt])

    def decodeString(self, s: str) -> str:
        i = 0
        ret = ""
        while i < len(s):
            if s[i].is_alpha():
                ret += s[i]
                i += 1
            else:
                q = i
                while s[q].is_digit(): q += 1
                q += 1
                cnt = 1
                while cnt != 0:
                    if s[q] == "[": cnt += 1
                    elif s[q] == "]": cnt -= 1
                    q += 1
                ret += self.decodeKString(s[i:q])
                i = q
        return ret

