import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        seen = set()
        def get_next_words(word):
            words = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet and next_word not in seen:
                        words.append(next_word)
            return words

        seen.add(beginWord)
        q = collections.deque([(beginWord, 0)])
        while len(q) != 0:
            word, cnt = q.popleft()
            if word == endWord: return cnt
            # get the next words
            words = get_next_words(word)
            seen.update(words)
            q += [(word, cnt+1) for word in words]
        return 0



