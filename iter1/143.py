class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        slow, fast = head, head.next
        # 1 2 | 3 4: slow = 2 fast = None
        # 1 2 3 | 4 5: slow = 3, fast = None
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        l1, slow.next, l2 = head, None, slow.next
        prev, first, second = None, l2, l2.next
        while second: first.next, second.next, prev, first, second = prev, first, first, second, second.next
        l2 = first
        pi, pj = l1, l2
        while pi and pj: pi.next, pi, pj.next, pj = pj, pi.next, pi.next, pj.next



