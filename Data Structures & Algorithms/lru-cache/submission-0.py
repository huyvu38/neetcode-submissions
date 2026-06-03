class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.left = Node(0,0)
        self.right = Node (0,0)
        self.left.next = self.right
        self.right.prev= self.left
    
    def add(self,node):
        prev = self.right.prev
        next = self.right
        node.prev=prev
        node.next=next
        prev.next=node
        next.prev=node

    def delete(self, node):
        prev = node.prev
        next = node.next
        prev.next =next
        next.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.map:
            #Remove to make it to recently use then add again
            self.delete(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])
        #Insert new
        self.map[key] = Node(key,value)
        self.add(self.map[key])

        if len(self.map) > self.cap:
            #find the least recently use -> next to left node
            lru = self.left.next
            self.delete(lru)
            del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)