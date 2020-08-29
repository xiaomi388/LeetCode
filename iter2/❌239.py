# 要点：queue中存index！
# https://zhuanlan.zhihu.com/p/26465701 单调栈的详细介绍
# https://zhuanlan.zhihu.com/p/26465701
# https://www.jianshu.com/p/a8f782b1a88a 总结了一些单调栈的题目
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, res = [], []
        for i in range(len(nums)):
            if len(queue) > 0 and i - queue[0] + 1 > k: del queue[0]
            while len(queue) > 0 and nums[i] > nums[queue[-1]]: del queue[-1]
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
