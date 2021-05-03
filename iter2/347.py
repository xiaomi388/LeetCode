class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnter = collections.Counter(nums)
        return list(map(lambda n : n[0], cnter.most_common(k)))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        cnter = collections.Counter(nums)
        hq = []
        # O(nlogk)
        for num, cnt in cnter.items():
            if len(hq) >= k:
                if hq[0][0] < cnt:
                    heapq.heappop(hq)
                else:
                    continue
            heapq.heappush(hq, (cnt, num))
        return list(map(lambda el : el[1], hq))




