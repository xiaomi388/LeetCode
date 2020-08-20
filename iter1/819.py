from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i, c in enumerate(paragraph):
            if not c.isalpha():
                paragraph = paragraph[:i] + " " + paragraph[i+1:]
        words = paragraph.split()
        cnt = defaultdict(int)
        for word in words:
            word = word.lower()
            if word in banned:
                continue
            cnt[word] += 1

        _max_cnt = -1
        _max_word = None
        for word in cnt:
            if cnt[word] > _max_cnt:
                _max_cnt = cnt[word]
                _max_word = word
        return _max_word




