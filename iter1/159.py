class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = dict()
        l, r = 0, 0
        for