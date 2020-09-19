class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = collections.defaultdict(list)
        for id, mgr in enumerate(manager): children[mgr].append(id)
        q = collections.deque([(headID, 0)])
        ans = 0
        while len(q):
            id, t = q.popleft()
            ans = max(ans, t)
            q += [(c, t+informTime[id]) for c in children[id]]
        return ans

