'''
0 <= len(list) <= 2 ** 31 - 1

Example 1:


   5<-2<-3<-4<-1<-o
      L
            R
            P  C  N
   S

      0  1  2  3  4
                  F
                <-1<-o
      5<-2<-3<-4
            P  C  N
         L     R
         S
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev, curr, next = dummy, head, head.next

        for _ in range(left-1):
            prev, curr, next = curr, next, next.next

        first, second = prev, curr
        #print(first.val, second.val)
        for _ in range(right-left):
            prev, curr, next = curr, next, next.next
            curr.next = prev
        first.next = curr
        second.next = next
        return dummy.next





