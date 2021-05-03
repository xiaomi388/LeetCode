class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        for i, num in enumerate(nums):
            self.pre_sum.append(num+self.pre_sum[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j+1] - self.pre_sum[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)