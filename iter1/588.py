from types import *

class FileSystem:

    def __init__(self):
        fs = {}

    def ls(self, path: str) -> List[str]:
        tokens = path.split('/')[1:]
        cd = self.fs
        for token in tokens:
            cd = cd[token]
        if isinstance(cd, dict):
            l = [k for k in cd]
            return l.sort()
        else:
            return tokens.split('/')[-1]


    def mkdir(self, path: str) -> None:
        tokens = path.split('/')[1:]
        cd = self.fs
        for token in tokens:
            if token not in cd:
                cd[token] = {}
            cd = cd[token]

    def addContentToFile(self, filePath: str, content: str) -> None:
        tokens = filePath.split('/')[1:]
        dirs = tokens[:-1]
        fileName = tokens[-1]
        cd = self.fs
        for dir in dirs:
            if dir not in cd:
                cd[dir] = {}
            cd = cd[dir]
        if fileName not in cd:
            cd[fileName] = content
        else:
            cd[fileName] += content


    def readContentFromFile(self, filePath: str) -> str:
        tokens = filePath.split('/')[1:]
        dirs = tokens[:-1]
        fileName = tokens[-1]
        cd = self.fs
        for dir in dirs:
            if dir not in cd:
                cd[dir] = {}
            cd = cd[dir]
        return cd[fileName]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

a = "1/2/3"
print(a.split('/'))


