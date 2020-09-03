# 单调栈

class StockSpanner:

    def __init__(self):
        self.q = collections.deque([(0, float('inf'))])
        self.cnt = 1


    def next(self, price: int) -> int:
        while self.q[-1][1] <= price: self.q.pop()
        ret = self.cnt - self.q[-1][0]
        self.q.append((self.cnt, price))
        self.cnt += 1
        return ret



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)