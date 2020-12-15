class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.counter(s) == collections.counter(t)
