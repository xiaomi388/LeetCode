# (n-1) = (a0-1) + 26*sum_{i=1}^m{a_m*26^{m-1}}

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        q, r = (columnNumber - 1) // 26, (columnNumber - 1) % 26
        return (self.convertToTitle(q) if q > 0 else "")  + chr(ord('A')+r)