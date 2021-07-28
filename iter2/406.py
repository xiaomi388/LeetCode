class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        out = []
        for h, k in people:
            i = len(out)
            out.append((h, k))
            while i != k:
                out[i], out[i - 1] = out[i - 1], out[i]
                i -= 1
        return out
