class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        d = set()
        i, q, ans = 0, 0, 0
        while True:
            while q - i < K:
                if q >= len(S):
                    return ans
                while S[q] in d:
                    d.discard(S[i])
                    i += 1
                d.add(S[q])
                q += 1
            ans += 1
            d.discard(S[i])
            i += 1


