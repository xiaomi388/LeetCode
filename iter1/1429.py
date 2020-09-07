# better way: use OrderedDict as deque
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.d = collections.Counter(nums)
        self.q = collections.deque(nums)

    def showFirstUnique(self) -> int:
        while len(self.q) and self.d[self.q[0]] > 1: self.q.popleft()
        return self.q[0] if len(self.q) else -1

    def add(self, value: int) -> None:
        self.d[value] += 1
        self.q.append(value)


