from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {str(k): [chr(ord("a") + (k-2)*3 + i) for i in range(3)] for k in range(2, 10) }
        m["9"].append("z")

        ans = []
        def dfs(i, output):
            if i == len(digits):
                ans.append(output)
                return

            for c in m[digits[i]]:
                output += c
                dfs(i+1, output)
                output = output[:-1]
        dfs(0, "")
        return ans




s = Solution()
print(s.letterCombinations(digits="23"))

