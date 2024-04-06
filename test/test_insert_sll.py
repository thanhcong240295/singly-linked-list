import sys
sys.path.append('../')

import unittest
from  singly_linked_list import init

class TestInsertSinglyLinkedList(unittest.TestCase):
  def test_insert_at_head(self):
    sll = init(10)
    sll.insert_at_head(11)
    self.assertEqual(sll.head.data, 11)

  def test_insert_at_tail_list_empty(self):
    sll = init(0)
    sll.insert_at_tail(11)
    
    current = sll.head
    
    while current.next:
       current = current.next

    self.assertEqual(sll.head.data, 11)
    self.assertEqual(current.data, 11)

  def test_insert_at_tail(self):
    sll = init(10)
    sll.insert_at_tail(11)
    
    current = sll.head
    
    while current.next:
       current = current.next

    self.assertEqual(sll.head.data, 1)
    self.assertEqual(current.data, 11)

  def test_insert_at_index_lester_than_zero(self):
    sll = init(10)
  
    self.assertEqual(sll.insert_at_index(11, -1), None)

  def test_insert_at_index_zero(self):
    sll = init(10)
    sll.insert_at_index(11, 0)

    self.assertEqual(sll.head.data, 11)

  def test_insert_at_index_grater_than_len(self):
    sll = init(10)
    sll.insert_at_index(20, 20)

    current = sll.head

    while current.next:
       current = current.next

    self.assertEqual(sll.head.data, 1)
    self.assertEqual(current.data, 20)

  def test_insert_at_index(self):
    sll = init(10)
    sll.insert_at_index(20, 5)

    self.assertEqual(sll.get_node_at_index(4).data, 5)
    self.assertEqual(sll.get_node_at_index(5).data, 20)
    self.assertEqual(sll.get_node_at_index(6).data, 6)

if __name__ == '__main__':
    unittest.main()
