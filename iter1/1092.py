class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        d = collections.defaultdict(list)
        for i, c in enumerate(str1):
            d[c].append(i)


        ans = None
        def dfs(i, pre_index, inserted):
            nonlocal ans
            if i == len(str2):
                ans = min(ans, inserted, key=lambda x : len(x))
                return
            # case 1: reuse
            idx = bisect.bisect_right(d[str2[i]], pre_index)
            if idx != len(str2):
                dfs(i+1, idx, inserted)
            # case 2: insert a new one
            dfs(i+1, pre_index+1, inserted+[pre_index+1])
        dfs(0, -1, [])
        for ins in inserted:
            str1.insert(ins, str2)



        return ans + len(str1)


