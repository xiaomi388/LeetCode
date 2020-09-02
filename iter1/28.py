class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # build next
        next = [0, 0]
        j, i = 0, 1
        for i in range(len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = next[j]
            if needle[i] == needle[j]:
                next.append(next[-1]+1)

        i, j = 0, 0
        for i in range(len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = next[j]
            if needle[j] == haystack[i]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1




