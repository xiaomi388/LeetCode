class Solution:
    def numSplits(self, s: str) -> int:
        left_cnter = defaultdict(int)
        right_cnter = defaultdict(int)

        out = 0

        for i in range(len(s)):
            right_cnter[s[i]] += 1

        for i in range(len(s)):
            left_cnter[s[i]] += 1
            right_cnter[s[i]] -= 1
            if right_cnter[s[i]] == 0:
                del right_cnter[s[i]]

            if len(left_cnter) == len(right_cnter):
                out += 1
        return out
