class Node:

  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None


class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.mp = {}
    # left = Least Recently Used (LRU) dummy head
    # right = Most Recently Used (MRU) dummy tail
    self.left = Node(0, 0)
    self.right = Node(0, 0)
    self.left.next = self.right
    self.right.prev = self.left

  # Remove a node from its current position in the linked list
  def _remove(self, node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  # Insert a node right before self.right (making it Most Recently Used)
  def _insert(self, node):
    prev_node = self.right.prev
    next_node = self.right

    prev_node.next = node
    node.prev = prev_node
    node.next = next_node
    next_node.prev = node

  def get(self, key: int) -> int:
    if key in self.mp:
      node = self.mp[key]
      # Move accessed node to MRU position
      self._remove(node)
      self._insert(node)
      return node.val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.mp:
      # Remove old node if key already exists
      self._remove(self.mp[key])

    # Create new node and insert at MRU position
    node = Node(key, value)
    self._insert(node)
    self.mp[key] = node

    # If over capacity, remove the LRU node (node right after self.left)
    if len(self.mp) > self.capacity:
      lru = self.left.next
      self._remove(lru)
      del self.mp[lru.key]
