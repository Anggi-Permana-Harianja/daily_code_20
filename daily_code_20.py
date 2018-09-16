'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def insert(self, val):
		#inser for the first time
		if self.head is None:
			self.head = Node(val)
			return

		new_node = Node(val)
		current = self.head
		while current.next:
			current = current.next

		current.next = new_node

	def print(self):
		current = self.head
		while current is not None:
			print(current.val, end = ' -> ')
			current = current.next

	def len(self):
		length = 0
		current = self.head
		while current is not None:
			length += 1
			current = current.next

		return length


A = LinkedList()
A.insert(3)
A.insert(7)
A.insert(8)
A.insert(10)
A.print()

print("")

B = LinkedList()
B.insert(99)
B.insert(1)
B.insert(8)
B.insert(10)
B.print()

print("")

def intersection(LinkedList_a, LinkedList_b):
	used_length = min(LinkedList_a.len(), LinkedList_b.len())
	a = LinkedList_a.head
	b = LinkedList_b.head

	for i in range(used_length):
		if a.val == b.val:
			return a.val
		else:
			a = a.next
			b = b.next

print(intersection(A, B))


