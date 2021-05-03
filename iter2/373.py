class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not len(nums1) or not len(nums2): return []
        hq = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        visited = set()
        while len(hq) and len(ans) < k:
            _, i, j = heapq.heappop(hq)
            if (i, j) in visited: continue
            ans.append((nums1[i], nums2[j]))
            visited.add((i, j))
            if i+1 < len(nums1):
                heapq.heappush(hq, (nums1[i+1]+nums2[j], i+1, j))
            if j+1 < len(nums2):
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))
        return ans




