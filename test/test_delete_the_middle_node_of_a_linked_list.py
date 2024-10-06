from typing import List, Optional
import unittest

from linked_lists.delete_the_middle_node_of_a_linked_list import Solution, ListNode


class TestDeleteTheMiddleNodeOfALinkedList(unittest.TestCase):
    def setUpListNode(self, array: List) -> ListNode:
        head = ListNode(array[0])
        head_copy = head
        for i in range(1, len(array)):
            head_copy.next = ListNode(array[i])
            head_copy = head_copy.next

        return head

    def linkedListToList(self, head: Optional[ListNode]) -> List[int]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def setUp(self):
        self.solution = Solution()
        self.list_node_odd = self.setUpListNode([1, 3, 4, 7, 1, 2, 6])
        self.list_node_even = self.setUpListNode([1, 2, 3, 4])
        self.list_node_two_nodes = self.setUpListNode([2, 1])
        self.list_node_one_node = self.setUpListNode([1])

    def testDeleteTheMiddleNodeOfAnOddListNode(self):
        self.result = self.solution.deleteMiddle(self.list_node_odd)
        self.expected_result = [1, 3, 4, 1, 2, 6]
        self.assertEqual(self.linkedListToList(self.result), self.expected_result)

    def testDeleteTheMiddleNodeOfAnEvenListNode(self):
        self.result = self.solution.deleteMiddle(self.list_node_even)
        self.expected_result = [1, 2, 4]
        self.assertEqual(self.linkedListToList(self.result), self.expected_result)

    def testDeleteTheMiddleNodeOfATwoNodesListNode(self):
        self.result = self.solution.deleteMiddle(self.list_node_two_nodes)
        self.expected_result = [2]
        self.assertEqual(self.linkedListToList(self.result), self.expected_result)

    def testDeleteTheMiddleNodeOfAOneNodeListNode(self):
        self.result = self.solution.deleteMiddle(self.list_node_one_node)
        self.expected_result = []
        self.assertEqual(self.linkedListToList(self.result), self.expected_result)
