# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:


class Solution:
    def __init__(self):
        self.cache = []

    def read(self, buf: List[str], n: int) -> int:
        if n == 0: return 0
        cnt = 0
        for i in range(min(len(self.cache), n)):
            buf[i] = self.cache[i]
            cnt += 1
            if cnt == n:
                self.cache = self.cache[cnt:]
                return n
        self.cache = []
        while True:
            buf4 = [" "] * 4
            n4 = read4(buf4)
            if n4 == 0: return cnt
            for i in range(n4):
                buf[cnt] = buf4[i]
                cnt += 1
                if cnt == n:
                    self.cache = buf4[i+1:n4]
                    return cnt



