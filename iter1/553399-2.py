# https://leetcode.com/discuss/interview-question/553399/

from collections import defaultdict

def Solution(s):
    left_cnter = defaultdict(int)
    right_cnter = defaultdict(int)

    out = 0

    for i in range(len(s)):
        right_cnter[s[i]] += 1

    for i in range(len(s)):
        left_cnter[s[i]] += 1
        right_cnter[s[i]] -= 1
        if right_cnter[s[i]] == 0:
            del right_cnter[s[i]]

        if len(left_cnter) == len(right_cnter):
            out += 1
    return out


if __name__ == "__main__":
    tests = [("aaaa", 3), ("bac", 0), ("ababa", 2), ("a", 0)]
    for test in tests:
        actual = Solution(test[0])
        if test[1] != actual:
            print(f'input={test[0]}, output={actual}, expected={test[1]}')