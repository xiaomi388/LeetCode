# count_node: 计算当前前缀下，可以最多得到多少个数字

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_node(prefix, max_n):
            prefix_next = prefix + 1
            cnt = 0
            prefix *= 10
            prefix_next *= 10
            while prefix <= max_n:
                cnt += min(prefix_next, max_n + 1) - prefix
                prefix *= 10
                prefix_next *= 10
            return cnt

        now_prefix = 1
        k -= 1
        while k > 0:
            tmp_cnt = count_node(now_prefix, n)
            if tmp_cnt >= k:
                now_prefix *= 10
                k -= 1
            elif tmp_cnt < k:
                now_prefix += 1
                k -= tmp_cnt + 1
        return now_prefix
