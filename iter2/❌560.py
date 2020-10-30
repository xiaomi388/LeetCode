# prefix_sum
# why can it work? because it uses hashmap to help
# find the previous valid positions in O(1) time
# instead of brute force looking for every subarray.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = collections.defaultdict(int)
        sum = ans = 0
        for i, num in enumerate(nums):
            sum += num
            ans += pre_sum[k-sum]
            pre_sum[sum] += 1
        return ans









