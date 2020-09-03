class Solution:
    def isUgly(self, num: int) -> bool:
        ret = False
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num % 2 == 0:
            ret = self.isUgly(num / 2)
        elif num % 3 == 0:
            ret = self.isUgly(num / 3)
        elif num % 5 == 0:
            ret = self.isUgly(num / 5)
        else:
            return False
        return ret

