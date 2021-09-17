class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        out = float('inf')
        for num in [tops[0], bottoms[0]]:
            is_valid = True
            top_cnt, bottom_cnt = 0, 0
            for i in range(len(tops)):
                if tops[i] != num and bottoms[i] != num:
                    is_valid = False
                    break
                if tops[i] == bottoms[i]:
                    continue
                elif tops[i] == num:
                    top_cnt += 1
                elif bottoms[i] == num:
                    bottom_cnt += 1
            if is_valid:
                out = min(out, min(top_cnt, bottom_cnt))
        return out if out != float('inf') else -1


