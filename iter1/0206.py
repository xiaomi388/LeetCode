# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def sizeof(head):
            i = 0
            while head is not None:
                head = head.next
                i += 1
            return i

        def get_tail(head):
            last = None
            while head is not None:
                last = head
                head = head.next
            return last

        def reverse(index):
            first = head
            for _ in range(index):
                first = first.next
            second = first.next
            while first is not None and second is not None:
                second.next, first, second = first, second, second.next

        def check(l1, l2, cnt):
            for _ in range(cnt):
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next
            return True

        if not head:
            return True
        size = sizeof(head)
        tail = get_tail(head)
        reverse(size // 2)
        return check(head, tail, size // 2)

