# 方法一：DP + TreeMap

import sortedcontainers
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)


        even_dp = [False] * n
        odd_dp = [False] * n

        even_dp[n-1] = True
        odd_dp[n-1] = True

        ss = sortedcontainers.SortedDict({A[n-1]: n-1})
        for i in range(n-2, -1, -1):
            # odd
            next = None
            q = ss.bisect_left(A[i])
            next = ss.values()[q] if q < len(ss) else None
            if next is not None:
                odd_dp[i] = even_dp[next]

            # even
            next = None
            q = ss.bisect_right(A[i])
            next = ss.values()[q-1] if q-1 >= 0 else None
            if next is not None:
                even_dp[i] = odd_dp[next]

            ss[A[i]] = i

        return collections.Counter(odd_dp)[True]

# 方法二： 单调栈
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i : A[i])
        oddnext = make(B)
        B.sort(key = lambda i : -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True
        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)


