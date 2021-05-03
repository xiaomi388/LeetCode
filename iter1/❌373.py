# 1 7 11
# 2 4 6
# 1 2 -> 3
# 1 4 -> 5

# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         if not len(nums1) or not len(nums2): return []
#         ans = []
#         min_i, min_q = 0, 0
#         i, q = 0, 0
#         while len(ans) < k and i < len(nums1) and q < len(nums2):
#             ans.append((nums1[i], nums2[q]))
#             candidates = []
#             c1, c2 = float('inf'), float('inf')
#             if i < len(nums1):
#                 c1 = nums1[i+1] + nums2[min_q]
#             else:
#                 min_q += 1
#             if q < len(nums2):
#                 c2 = nums2[q+1] + nums1[min_i]
#             else:
#                 min_i += 1
#             if c1 < c2:
#                 i += 1
#                 q = min_q
#             else:
#                 q += 1
#                 i = min_i
#         return ans


# https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/solution/pyhont3yi-xing-jie-fa-dao-gao-xiao-jie-fa-by-ml-zi/
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs




