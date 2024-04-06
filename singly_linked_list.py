class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.next = None
    
class SinglyLinkedList:
  def __init__(self) -> None:
    self.head = None

  def insert_at_head(self, data: int):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  
  def insert_at_tail(self, data: int):
    node_len = self.get_len()

    if (node_len == 0):
      return self.insert_at_head(data)

    new_node = Node(data)
    current = self.head

    while current.next:
      current = current.next
    current.next = new_node

  def insert_at_index(self, data: int, index: int):
    if (index < 0):
      return None
    
    if (index == 0):
      return self.insert_at_head(data)

    node_len = self.get_len()
    if (index >= node_len):
      return self.insert_at_tail(data)
    
    new_node = Node(data)
    prev_node = self.get_node_at_index(index - 1)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_first_node(self):
    if (self.head is None):
      return None

    new_first_node = self.head.next
    self.head = new_first_node

  def delete_last_node(self):
    if (self.head is None or self.head.next is None):
      return self.delete_first_node()
    
    node_len = self.get_len()
    prev_node = self.get_node_at_index(node_len - 2)
    prev_node.next = None

  def delete_node_at_index(self, index: int):
    if (self.head is None or index < 0):
      return None
    
    if (index == 0):
      return self.delete_first_node()
    
    if (index >= self.get_len() - 1):
      return self.delete_last_node()
    
    prev_node = self.get_node_at_index(index - 1)
    del_node = self.get_node_at_index(index)
    next_node = del_node.next

    prev_node.next = next_node

  def get_node_at_index(self, index: int):
    node_len = self.get_len()

    if (index < 0 or index > node_len):
      return

    if (index == 0):
      return self.head
    
    current = self.head
    for i in range(0, index):
      current = current.next

    return current

  def get_len(self) -> int:
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  def display(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next

def init(len: int):
  sll = SinglyLinkedList()

  for i in range(0, len):
    sll.insert_at_tail(i + 1)

  return sll
