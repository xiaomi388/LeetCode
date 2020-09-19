class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # Because the count of local inversion should
        # be less than or equal to count of global,
        # all we care is when local less than global happens.
        # The difference between local and global is global
        # also include nonadjacent i and j, so simplify
        # the question to for every i, find in range 0 to i minus
        # 2, see if there is an element larger than A[i]. If it
        # exists, we can return false directly.
        m = -1
        for i, num in enumerate(A[:-2]):
            max = max(max, num)
            if max >= A[i+2]: return False
        return True










