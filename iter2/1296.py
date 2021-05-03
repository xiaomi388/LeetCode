class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = collections.Counter(nums)
        nums = sorted(s)
        for num in nums:
            occ = s[num]
            if occ > 0:
                for i in range(num+1, num+k):
                    if s[i] < occ:
                        return False
                    s[i] -= occ
        return True