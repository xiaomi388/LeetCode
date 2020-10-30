# Observation: we actually don't care the number of vowels,
# what we care is for every vowel, can it be mod by 2
# (whether the number of it is even or odd)
# so we can build a prefix state to store the vowels'
# even/odd states of subarray s[:i].
# whenever we check the longest valid subarray end in the position i,
# we can simply find the previous position which
# has the same "even/odd states".
# As for how to represent this state, we can use
# a binary array to represent it, so that
# 00000 means all numbers of vowels are even,
# 11111 means all numbers of vowels are odd

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        cur = ans = 0
        for i, c in enumerate(s):
            cur ^= (1 << ("aeiou".find(c)+1)) >> 1
            seen.setdefault(cur, i)
            ans = max(ans, i-seen[cur])
        return ans










