# TODO

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d, dgr = collections.defaultdict(set), collections.defaultdict(int)
        for i in range(len(words)-1):
            for q in range(min(len(words[i]), len(words[i-1]))):
                if words[i][q] != words[i+1][q]:
                    d[words[i][q]].add(d[words[i+1][q]])
                    dgr[words[i][q]] = dgr[words[i][q]]
                    dgr[words[i+1][q]] += 1

        # MST
        q = collections.deque([c for c in dgr if dgr[c] == 0])
        if len(q) > 1:
            return ""
        ans = ""
        while len(q):
            c = q.popleft()
            ans += c
            for child in d[c]:
                dgr[child] -= 1
                if dgr[child] == 0:
                    q.append(child)
        if len(ans) != len(dgr):
            return ""
        return ans








