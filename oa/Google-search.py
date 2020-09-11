class Solution:
    def search(self, users, n):
        events = []
        for user, (login, logout) in enumerate(users):
            events.append((login, user, True))
            events.append((logout, user, False))
        events.sort()

        most_searched, least_searched = 0, 0

        ans = [None] * len(users)

        for ts, user, login in events:
            if login:
                ans[user] = (least_searched+1, 0)
                most_searched += 1
            else:
                ans[user] =  (ans[user][0], most_searched)
                least_searched += 1
        print(ans)

s = Solution()
s.search([[0, 100], [101, 200]], 2)




