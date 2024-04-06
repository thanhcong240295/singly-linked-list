import sys
sys.path.append('../')

import unittest
from  singly_linked_list import init

class TestGetSinglyLinkedList(unittest.TestCase):
  def test_get_node_at_index_less_than_zero(self):
    sll = init(10)
    self.assertEqual(sll.get_node_at_index(-1), None)

  def test_get_node_at_index_zero(self):
    sll = init(10)
    sll.get_node_at_index(0)
    self.assertEqual(sll.head.data, 1)

  def test_get_node_at_index(self):
    sll = init(10)
    self.assertEqual(sll.get_node_at_index(5).data, 6)

if __name__ == '__main__':
    unittest.main()
