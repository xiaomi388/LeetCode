class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(int(''.join(map(lambda x : str(x), digits)))+1)