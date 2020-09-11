class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # create dict for all synonyms
        # d stands for the next synonym, p stands for which group
        # a word belongs to
        d, p = {}, {}
        for k, v in synonyms:
            d[k] = v
            if k not in p:
                p[k] = k
            p[v] = p[k]

        # split words in text
        text = text.split()

        # store all indexes of synonyms words in text
        poses = [i for i, word in enumerate(text) if word in d]

        # dfs for all poses
        ans = []
        def dfs(idx, text):
            if idx == len(poses):
                # append the text to the ans list
                # remember to form a string from the text array
                ans.append(' '.join(text))
                return

            # replace the word in pos poses[idx] of text
            # by its synonym
            ori_word, new_word = text[poses[idx]], d[text[poses[idx]]]

            # because the new word may have synonym
            # so we should keep transforming it until
            # there is no synonym
            while True:
                text[poses[idx]] = new_word
                # dfs
                dfs(idx+1, text)
                if new_word == ori_word:
                    break
                if new_word in d:
                    new_word = d[new_word]
                else:
                    new_word = p[new_word]
        dfs(0, text)
        return sorted(ans)
