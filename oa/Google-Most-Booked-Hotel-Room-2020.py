class Solution:
    def MostBookedHetelRoom(self, events):
        return len(set([e for e in events if e[0] == "+"]))

s = Solution()
inputs = [["+0A","+9Z","+4F","-9Z"], ["+4B","-4B","+4B","-4B"]]
for i in inputs:
    print(s.MostBookedHetelRoom(i))


