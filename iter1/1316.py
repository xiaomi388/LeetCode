class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        seen = set()
        for i in range(len(text)):
            for q in range(i+1, len(text), 2):
                if text[i:(i+q)//2+1] == text[(q+i)//2+1:q+1]:
                    seen.add(text[i:(i+q)//2+1])
        return len(seen)

