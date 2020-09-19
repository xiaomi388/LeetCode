class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x : x[0])
        slots2.sort(key=lambda x : x[0])

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            # calculate the common duration
            d = min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0])
            if d >= duration:
                return [st := max(slots1[i][0], slots2[j][0]), st + duration]
            if slots1[i][0] < slots2[j][0]:
                i += 1
            else:
                j += 1
        return []

