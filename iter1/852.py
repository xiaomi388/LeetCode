class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        k = 0
        for i in range(len(A)):
            if A[i] == B[i]: continue
            k += 1
            found = False
            for q in range(i+1, len(A)):
                if A[i] == B[q] and B[i] == A[q]:
                    A[i], A[q] = A[q], A[i]
                    found = True
                    break
            if found: continue
            for q in range(i+1, len(A)):
                if B[i] == A[q]:
                    A[i], A[q] = A[q], A[i]
                    break
        return k