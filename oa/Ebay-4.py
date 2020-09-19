def digitAnagrams(a):
    d = dict()
    for num in a:
        hash = [0] * 10
        for digit in str(num):
            hash[int(digit)] += 1
        hash = tuple(hash)
        d[hash] = d.get(hash, 0) + 1
    ans = 0
    for v in d.values():
        if v <= 1: continue
        ans += (v * (v-1)) / 2
    return int(ans)

print(digitAnagrams([25, 35, 872, 228, 53, 278, 872]))

