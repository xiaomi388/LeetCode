def mergingLetters(s, t):
    ans = ""
    i, j = 0, 0
    while i < len(s) and j < len(t):
        ans += s[i] + t[j]
    while i < len(s): ans += s[i]
    while j < len(t): ans += t[j]
    return ans
