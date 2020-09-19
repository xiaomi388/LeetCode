# Python(since 3.5) dict keeps the order!!

class Leaderboard:

    def __init__(self):
        self.players = {}
        self.scores = sortedcontainers.SortedSet()


    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] = score
        self.scores.add((score, playerId))


    def top(self, K: int) -> int:
        return sum([s for p, s in self.scores.items()[-k:]])


    def reset(self, playerId: int) -> None:
        self.scores.discard((playerId, self.players[playerId]))
        del self.players[playerId]



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)