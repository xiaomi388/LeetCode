# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        valid = [set() for i in range(6)]
        invalid = [set() for i in range(6)]
        words = set(wordlist)

        for word in wordlist:
            val = master.guess(word)
            if val == 0:
                for

