class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # Group points with the same y value
        d = collections.defaultdict(list)
        for point in points: # n
            d[point[1]].append(point[0])

        c = None
        for y in d: # klogk * (n / k) = nlogk
            d[y].sort()
            i, q = 0, len(d[y])-1
            while i <= q:
                if c is None:
                    c = (d[y][i] + d[y][q]) / 2
                else:
                    if (d[y][i] + d[y][q]) / 2 != c:
                        return False
                i += 1
                q -= 1
        return True



