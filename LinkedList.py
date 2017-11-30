class Node(object):
	def __init__(self, data):
		self.data = data
		self.next_node = None
		self.prev_node = None


class LinkedList(object):
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next_node = self.head
			new_node.next_node.prev_node = new_node
			self.head = new_node

	def __str__(self):
		s = ""
		p = self.head
		if p is not None:
			while p.next_node is not None:
				s += p.data
				p = p.next_node

			s += p.data
		return s

if __name__ == '__main__':
	l = LinkedList()
	l.insert('a')
	l.insert('b')
	l.insert('c')

	print l
