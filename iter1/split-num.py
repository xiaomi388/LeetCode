# 给int A， A可以被切成a,b两个数，求|a-b|的最小值。eg: int A = 235, when a=2,b=35,then |a-b| = 32; when a = 23,b=5,then |a-b| = 18, 返回18

def Solution(s):
    out = float('inf')
    for i in range(1, len(s)):
        out = min(out, abs(int(s[:i])-int(s[i:])))
    return out

if __name__ == "__main__":
    tests = [("12001", 11), ("510", 5), ("000", 0)]
    for input, expected in tests:
        actual = Solution(input)
        if actual != expected:
            print(input, actual, expected)
