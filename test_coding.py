class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = None

	def add_next(self,next_val):
		self.next= next_val

class Linked_list(object):
	
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self,data):
		n = Node(data)
		if self.head == None:
			self.head = n
			self.tail = n
		else:
			self.tail.next = n
			self.tail.next.next = None
			self.tail = n

	def remove_node(self,key):
		if self.head == None:
			return -1
		if self.head.data == key:
			self.head = self.head.next
			return 1

		prev = self.head
		loop_p = prev.next
		while loop_p != None:
			if loop_p.data == key:
				prev.next = loop_p.next
				if prev.next != None:
					loop_p = prev.next
			prev = loop_p
			loop_p = loop_p.next

	def reverse_ll(self):
		if self.head == None or self.head.data == self.tail.data:
			return -1 
		prev = None
		current = self.head
		next_n = current.next
		self.tail = current
		while True:
			current.next = prev
			prev = current
			current = next_n
			if current == None:
				break
			self.head = current
			next_n = next_n.next
		return 1




	def print_list(self):
		loop_p = self.head
		while loop_p != None:
			print(loop_p.data)
			loop_p = loop_p.next

def add_link(l1,l2):
		l3 = Linked_list()
		c1 = l1.head
		c2 = l2.head
		carry = 0
		while c1 != None:
			s = c1.data + c2.data + carry	
			if s > 10:
				carry = s - 10
				if c1.next != None:
					s = int(s/10)
			l3.add_node(s)
			c1 = c1.next
			c2 = c2.next
		return l3

ll = Linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
# ll.remove_node(4)
ll.remove_node(3)
ll.remove_node(5)
ll.print_list()
print('---reverse ll---')
ll.reverse_ll()
ll.print_list()
print('---test sum---')
l1 = Linked_list()
l1.add_node(4)
l1.add_node(2)
l1.add_node(1)
l2 = Linked_list()
l2.add_node(7)
l2.add_node(5)
l2.add_node(9)
l3 = add_link(l1,l2)
l3.print_list()
