# So that in each round we will repair the first unordered character and as a result move
# forward at least 1 step.
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        seen = set()
        q = collections.deque([(A, 0)])
        while len(q):
            s, k = q.popleft()
            seen.add(s)
            if s == B: return k
            for i in range(len(s)):
                for q in range(i+1, len(s)):
                    next_s = list(s)
                    next_s[i], next_s[q] = next_s[q], next_s[i]
                    next_s = str(next_s)
                    if next_s in seen: continue
                    q.append((next_s, k+1))
        return float('inf')
