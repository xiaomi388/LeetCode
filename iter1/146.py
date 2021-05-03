# 1.  In an assignment statement, the right-hand side is always evaluated fully before doing
# the actual setting of variables !!!
#
# 2. modify the size only after we inserted a new key!!!

class ListNode:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.head = ListNode(None, None, None, None)
        self.head.prev, self.head.next = self.head, self.head
        self.capacity = capacity
        self.hash = {}


    def get(self, key: int) -> int:
        #print(key)
        if key not in self.hash:
            return -1
        node = self.hash[key]
        node.prev.next, node.next.prev = node.next, node.prev
        node.next, node.prev, self.head.next.prev, self.head.next = self.head.next, self.head, node, node
        #self.print()
        return self.hash[key].val


    def put(self, key: int, value: int) -> None:
        #print(key, value)
        if key not in self.hash:
            self.hash[key] = ListNode(key, value, self.head, self.head.next)
            node = self.hash[key]
            self.head.next.prev, self.head.next = node, node
            if self.size < self.capacity:
                self.size += 1
            else:
                node = self.head.prev
                self.head.prev.prev.next, self.head.prev = self.head, self.head.prev.prev
                del self.hash[node.key]
        else:
            node = self.hash[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
            node.next, node.prev, self.head.next.prev, self.head.next = self.head.next, self.head, node, node


        #self.print()

    def print(self):
        cnt = 0
        cur = self.head.next
        ans = []
        while cur != self.head and cnt < 10:
            ans.append(cur.key)
            cur = cur.next
            cnt += 1


        r_ans = []
        cur = self.head.prev
        cnt = 0
        while cur != self.head and cnt < 10:
            r_ans.append(cur.key)
            cur = cur.prev
            cnt += 1
        print(ans, r_ans)







class ListNode:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.head = ListNode(None, None, None, None)
        self.head.prev, self.head.next = self.head, self.head
        self.capacity = capacity
        self.hash = {}


    def get(self, key: int) -> int:
        print(key)
        self.print()
        if key not in self.hash:
            return -1
        node = self.hash[key]
        node.prev.next, node.next.prev = node.next, node.prev
        node.next, node.prev, self.head.next.prev, self.head.next = self.head.next, self.head, node, node
        print("head:", self.head.val)
        self.print()
        return self.hash[key].val


    def put(self, key: int, value: int) -> None:
        print(key, value)
        print("head:", self.head.val)
        if key not in self.hash:
            self.hash[key] = ListNode(key, value, self.head, self.head.next)
            node = self.hash[key]
            self.head.next.prev, self.head.next = node, node
        else:
            node = self.hash[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
            node.next, node.prev, self.head.next.prev, self.head.next = self.head.next, self.head, node, node
        if self.size < self.capacity:
            self.size += 1
        else:
            node = self.head.prev
            self.head.prev.prev.next, self.head.prev = self.head.prev.prev, self.head
            self.print()
            del self.hash[node.key]
        self.print()

    def print(self):
        cnt = 0
        cur = self.head.next
        ans = []
        while cur != self.head and cnt < 10:
            ans.append(cur.val)
            cur = cur.next
            cnt += 1
        print(ans)



