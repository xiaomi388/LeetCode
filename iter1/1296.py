from sortedcontainers import SortedList

# brute force
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if nums % k != 0: return False

        nums = SortedList(nums)
        row = []
        i = 0
        while i < len(nums):
            if len(row) == k:
                row = []
                i = 0
            elif not row or nums[i] == row[-1] + 1:
                row.append(nums[i])
                del nums[i]
            else:
                i += 1
        return False if nums else True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = collections.Counter(nums)
        ordered_nums = sorted(s)
        for num in ordered_nums:
            occ = s[num]
            if s[num] > 0:
                for i in range(num + 1, num + k):
                    if s[i] >= occ:
                        s[i] -= occ
                    else:
                        return False
        return True





