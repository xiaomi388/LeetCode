from functools import lru_cache
class Solution:
    def encode(self, s: str) -> str:
        @lru_cache(None)
        def _encode(begin, end):
            if begin >= end: return ""

            cur_s = s[begin:end]
            if len(cur_s) <= 4: return cur_s

            ans = cur_s
            for i in range(begin+1, end):
                pre, suf = _encode(begin, i), _encode(i, end)
                if len(pre) + len(suf) < len(ans):
                    ans = pre + suf

            for i in range(begin+1, end):
                # check if we can compress two substring
                pattern = s[begin:i]
                if cur_s.replace(pattern, "") == "":
                    candidate = f"{str(len(cur_s) // len(pattern))}[{_encode(begin, i)}]"
                    if len(candidate) < len(ans):
                        ans = candidate
            return ans
        return _encode(0, len(s))

