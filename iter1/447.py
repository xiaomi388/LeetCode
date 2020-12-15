# brute force: take every three points, for every order, check if it is a boomerangs
# time complexity: O(C(n, 3)*6) = O(n^3)
# optimization: hashmap

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist_of(p1, p2):
            return abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2

        ans = 0
        for i in range(len(points)):
            dist = collections.defaultdict(int)
            for q in range(len(points)):
                if i == q: continue
                dist[dist_of(points[i], points[q])] += 1
            for cnt in dist.values():
                ans += cnt*(cnt-1)
        return ans


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        def dist(p1, p2):
            return abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2

        def check(points):
            # get the element in the middle
            e1 = dist(points[0], points[1])
            e2 = dist(points[0], points[2])
            e3 = dist(points[1], points[2])
            return e1 == e2 or e1 == e3 or e3 == e2

        def dfs(picked, i):
            """

            :param picked: picked points
            :param i: can only choose points after position i
            :return:
            """
            nonlocal ans
            if len(picked) == 3 and check(picked):
                #print(picked)
                ans += 2
            elif i >= len(points):
                return
            else:
                dfs(picked+[points[i]], i+1)
                dfs(picked, i+1)
        dfs([], 0)
        return ans
