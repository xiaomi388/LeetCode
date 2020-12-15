class Solution:
    def maxRepOpt1(self, text: str) -> int:
        d = {c: [i for i, ch in text if ch == c] for c in set(text)}

        ans = 0
        for c, idxes in d:
            pre, cur, max_sum = 0, 0, 0
            for i in range(len(idxes)):
                if i == 0 or idxes[i] == idxes[i-1]+1:
                    cur += 1
                elif idxes[i] == idxes[i-1]+2:
                    pre, cur = cur, 1
                else:
                    pre, cur = 0, 1
                max_sum = max(max_sum, pre+cur)
            ans = max(ans, max_sum+ 1 if len(max_sum)!=len(idxes) else 0)
        return ans




if __name__ == "__main__":
    s = Solution
    s.maxRepOpt1("abcdaaa")
