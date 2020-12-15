class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return head
        odd, even = head, head.next
        first, second = odd, even
        while second and second.next:
            first.next, second.next, first, second = second.next, second.next.next, second.next, second.next.next
        first.next = even
        return head
