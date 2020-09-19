class Solution:
    def __init__(self):
        self.history = []
        self.pasteboard = ""

    def insert(self, s):
        cur_text = self.history[-1] if len(self.history) else ""
        cur_text += s
        self.history.append(cur_text)

    def delete(self):
        cur_text = self.history[-1] if len(self.history) else ""
        cur_text = cur_text[:-1]
        self.history.append(cur_text)

    def copy(self, i):
        cur_text = self.history[-1] if len(self.history) else ""
        self.pasteboard = cur_text[i:]

    def paste(self):
        if len(self.pasteboard) == 0:
            return
        cur_text = self.history[-1] if len(self.history) else ""
        cur_text += self.pasteboard
        self.history.append(cur_text)

    def undo(self):
        if len(self.history):
            self.history.pop()

s = Solution()
s.insert("Code")
s.insert("Signal")
s.delete()
s.undo()
s.copy(4)
s.paste()
print(s.history)
