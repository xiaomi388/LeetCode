# 1. divide string into groups
# 2. scan all groups and judge if the group is valid

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def process(s):
            groups, group = [], None
            for i, c in enumerate(s):
                if i == 0:
                    group = (c, 0)
                elif c != s[i-1]:
                    groups.append(group)
                    group = (c, 0)
                group = (group[0], group[1]+1)
            if group: groups.append(group)
            return groups

        ret = len(words)
        S_grps = process(S)
        words_grps = [process(word) for word in words]
        for word_grps in words_grps:
            if len(S_grps) != len(word_grps):
                ret -= 1
                continue
            for i, word_grp in enumerate(word_grps):
                S_grp = S_grps[i]
                if (word_grp[0] != S_grp[0] or
                        word_grp[1] > S_grp[1] or
                        (word_grp[1] < S_grp[1] and S_grp[1] < 3)):
                    ret -= 1
                    break
        return ret
