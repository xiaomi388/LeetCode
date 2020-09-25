
INF = 2147483647

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        que = collections.deque()
        for r in range(len(rooms)):
            for c in len(rooms[0]):
                if rooms[r][c] == 0:
                    que.push((r, c, 0))

        seen = set()
        while len(que):
            r, c, dist = que.popleft()
            rooms[r][c] = dist
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                tx, ty = r+dx, c+dy
                if (0 <= tx < len(rooms) and 0 <= ty < len(rooms[0]) and
                        (tx, ty) not in seen and rooms[tx][ty] == INF):
                    seen.add((tx, ty))
                    que.push((tx, ty, dist+1))
