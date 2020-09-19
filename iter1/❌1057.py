class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist_of(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        conns = sorted([(dist_of(w_cord, b_cord), worker, bike)
                        for bike,b_cord in enumerate(bikes)
                        for worker, w_cord in enumerate(workers)])
        #print(conns)

        ans = [None] * len(workers)
        bike_used = set()
        for dist, worker, bike in conns:
            if len(bike_used) == len(workers): break
            #print(dist, worker, bike)
            if ans[worker] is None and bike not in bike_used:
                ans[worker] = bike
                bike_used.add(bike)
        return ans






