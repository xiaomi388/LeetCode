import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Params:
    cost: int
    cord: Any = field(compare=False)

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        def findNextCords(cord):
            nextCords = []
            nextCosts = []
            for i, q in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nextCord = list(cord)
                nextCost = 0
                while (0 <= nextCord[0] < len(maze) and 0 <= nextCord[1] < len(maze[0]) and
                       maze[nextCord[0]][nextCord[1]] != 1):
                    nextCord[0] += i
                    nextCord[1] += q
                    nextCost += 1
                nextCords.append((nextCord[0]-i, nextCord[1]-q))
                nextCosts.append(nextCost-1)
            return nextCords, nextCosts

        visited = set()
        queue = [Params(0, tuple(start))]
        while len(queue):
            param = heapq.heappop(queue)
            cost = param.cost
            cord = param.cord

            if cord[0] == destination[0] and cord[1] == destination[1]:
                return cost
            if cord in visited:
                continue

            visited.add(cord)
            nextCords, nextCosts = findNextCords(cord)
            for i in range(len(nextCords)):
                heapq.heappush(queue, Params(cost+nextCosts[i], nextCords[i]))
        return -1

