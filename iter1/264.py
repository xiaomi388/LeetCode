# TODO:???
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i, j, k = 0, 0, 0
        for _ in range(n-1):
            num = min(nums[i]*2, nums[j]*3, nums[k]*5)
            nums.append(num)
            if num == nums[i] * 2: i += 1
            if num == nums[j] * 3: j += 1
            if num == nums[k] * 5: k += 1
        return nums[-1]


