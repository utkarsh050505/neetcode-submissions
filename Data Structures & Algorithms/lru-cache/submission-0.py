class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        nxt_node = node.next
        prev_node = node.prev
        prev_node.next = nxt_node
        nxt_node.prev = prev_node
        return
    
    def _add_to_tail(self, node: Node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_head = self.head.next
                self._remove(lru_head)
                del self.cache[lru_head.key]
            
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_tail(node)