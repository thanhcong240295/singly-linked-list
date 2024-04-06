import sys
sys.path.append('../')

import unittest
from  singly_linked_list import init

class TestDeleteSinglyLinkedList(unittest.TestCase):
  def test_delete_first_node_list_empty(self):
    sll = init(0)
    sll.delete_first_node()
    self.assertEqual(sll.delete_first_node(), None)

  def test_delete_first_node_only_one(self):
    sll = init(1)
    sll.delete_first_node()
    self.assertEqual(sll.get_len(), 0)
    self.assertEqual(sll.head, None)

  def test_delete_first_node(self):
    sll = init(10)
    sll.delete_first_node()
    self.assertEqual(sll.get_len(), 9)
    self.assertEqual(sll.head.data, 2)

  def test_delete_last_node_list_empty(self):
    sll = init(0)
    sll.delete_last_node()
    self.assertEqual(sll.delete_first_node(), None)

  def test_delete_first_node_only_one(self):
    sll = init(1)
    sll.delete_last_node()
    self.assertEqual(sll.get_len(), 0)
    self.assertEqual(sll.head, None)

  def test_delete_first_node(self):
    sll = init(10)
    sll.delete_last_node()
    self.assertEqual(sll.get_len(), 9)
    self.assertEqual(sll.get_node_at_index(8).next, None)

  def test_delete_node_at_index_list_empty(self):
    sll = init(0)
    self.assertEqual(sll.delete_node_at_index(1), None)

  def test_delete_node_at_index_index_less_than_zero(self):
    sll = init(10)
    self.assertEqual(sll.delete_node_at_index(-1), None)
    self.assertEqual(sll.get_len(), 10)

  def test_delete_node_at_index_index_less_zero(self):
    sll = init(10)
    sll.delete_node_at_index(0)
    self.assertEqual(sll.head.data, 2)
    self.assertEqual(sll.get_len(), 9)

  def test_delete_node_at_index_index_greater_than_list_len(self):
    sll = init(10)
    self.assertEqual(sll.delete_node_at_index(20), None)

  def test_delete_node_at_index_index(self):
    sll = init(10)
    sll.delete_node_at_index(5)
    self.assertEqual(sll.get_node_at_index(4).data, 5)
    self.assertEqual(sll.get_node_at_index(5).data, 7)

if __name__ == '__main__':
    unittest.main()
