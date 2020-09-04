# 求三个数的并集

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            tmp = x % y
            if tmp > 0:
                return gcd(y, tmp)
            return y

        def lcm(x, y):
            return x * y // gcd(x, y)

        lo, hi = 0, min(a, b, c) * n
        while lo <= hi:
            mid = (lo + hi) // 2
            cnt =mid // a + mid // b + mid // c - mid // lcm(a, b) - mid // lcm(b, c) - mid // lcm(a, c) + mid // lcm(lcm(a, b), c)
            if cnt == n:
                if any([mid % i == 0 for i in [a, b, c]]): return mid
                hi = mid - 1
            elif cnt > n: hi = mid-1
            else: lo = mid + 1
        return lo

