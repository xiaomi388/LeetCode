class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min([len(str) for str in strs])
        for i in range(m):
            for q in range(len(strs)-1):
                if strs[q][i] != strs[q][i+1]:
                    return strs[0][:i]
        return m

# 骚操作：zip
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        objs = zip(*strs)
        for obj in objs:
            s = set(obj)
            if len(s) == 1:
                ret += obj[0]
            else:
                break
        return ret






