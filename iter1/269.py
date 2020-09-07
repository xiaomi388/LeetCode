class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d, rd = {}, {}
        for i in range(len(words)-1):
            for q in range(min(len(words[i]), len(words[i-1]))):
                if words[i][q] != words[i+1][q]:
                    if words[i][q] not in d:
                        d[words[i][q]] = set()
                    d[words[i][q]].add(d[words[i+1][q]])
                    if words[i+1][q] not in rd:
                        d[words[i+1][q]] = set()
                    d[words[i+1][q]].add(d[words[i][q]])

        start = None
        for c in d:
            if c not in rd:
                start = c
                break
        end = None
        for c in rd:
            if c not in d:
                end = c
                break
        if not start or not end: return ""

        # MST
        ret = start
        while ret < n := len(d+1)





