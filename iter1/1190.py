# key point: only when search to right bracket can we know the begin and end position of a word.
# so we should use stack to emulate this process.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            # remove the innerest word
            if s[i] == ")":
                word = ""
                while st[-1] != "(":
                    word += st.pop()
                st.pop()
                st += list(word)
            else:
                st.append(s[i])
        #print(st)
        return ''.join(st)