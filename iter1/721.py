from typing import *
from sortedcontainers import SortedList
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        p, r, n = {}, {}, {}

        def find(x):
            if x not in p:
                p[x], r[x] = x, 0
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if r[px] > r[py]: p[py] = px
            elif r[px] < r[py]: p[px] = py
            else:
                p[py] = px
                r[px] += 1

        for name, *emails in accounts:
            find(emails[0])
            for i in range(1, len(emails)):
                union(emails[i], emails[i-1])
            n[find(emails[0])] = name

        ans = collections.defaultdict(SortedList)
        for email in p:
            ans[(find(email), n[find(email)])].add(email)
        return [[k[1], *v] for k, v in ans.items()]



