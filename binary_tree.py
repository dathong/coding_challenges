class Node(object):

	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

class BST(object):

	def __init__(self,node=None):
		self.root = node

	def insert_value(self, value):



		def insert_until(node, root):

			if node.value > root.value:
				if root.right == None:
					root.right = node
				else:
					insert_until(node, root.right)
			else:
				if root.left == None:
					root.left = node
				else:
					insert_until(node, root.left)
		n = Node(value,None,None)
		if self.root == None:
			self.root = n
			return
		insert_until(n,self.root)

	def in_order(self):

		def in_order_until(root):
			if root == None:
				return
			print(root.value)
			in_order_until(root.left)
			in_order_until(root.right)
			
		in_order_until(self.root)

	def is_balance(self):
		self.min_val = 99999
		self.max_val = 0

		def in_order_until(root,depth=0):
			if root == None:
				if depth > self.max_val:
					self.max_val = depth
				if depth < self.min_val:
					self.min_val = depth
				return
			print(root.value)
			in_order_until(root.left,depth+1)
			in_order_until(root.right,depth+1)

		in_order_until(self.root,0)
		if self.max_val - self.min_val > 1:
			return False, self.min_val, self.max_val
		return True, self.min_val, self.max_val

	def find_height(self):
		def height_util(root):
			if root == None:
				return 0
			else:
				return max(height_util(root.left),height_util(root.right)) + 1
		return height_util(self.root)

	def find_sum_path(self,find_sum):

		def find_sum_util(root,find_sum,sum_so_far,carry_path):
			if root == None:
				return False
			carry_path.append(root.value)
			if sum_so_far + root.value == find_sum:
				return True
			return find_sum_util(root.left,find_sum,sum_so_far + root.value,carry_path) \
			or find_sum_util(root.right,find_sum,sum_so_far + root.value,carry_path)
		
		return find_sum_util(self.root,find_sum,0,[])  \
			or find_sum_util(self.root.left,find_sum,0,[]) \
			or find_sum_util(self.root.right,find_sum,0,[]) 		

	def find_sum_path_withpath(self,find_sum):

		def find_sum_util(root,find_sum,sum_so_far,carry_path):
			if root == None:
				return False
			carry_path.append(root.value)
			if sum_so_far + root.value == find_sum:
				print('path = ',carry_path)
				return True
			return find_sum_util(root.left,find_sum,sum_so_far + root.value,carry_path) \
			or find_sum_util(root.right,find_sum,sum_so_far + root.value,carry_path)
		
		return find_sum_util(self.root,find_sum,0,[])  \
			or find_sum_util(self.root.left,find_sum,0,[]) \
			or find_sum_util(self.root.right,find_sum,0,[])


	def find_acestor(self,v1,v2):

		def in_order_util(root,parent_dict,parent):
			if root == None:
				return
			parent_dict[root.value] = parent
			in_order_util(root.left,parent_dict,root.value)
			in_order_util(root.right,parent_dict,root.value)
		parent_dict = {}
		in_order_util(self.root,parent_dict,None)
		print('parent_dict = ',parent_dict)
		if v1 not in parent_dict or v2 not in parent_dict:
			return None
		#--track---
		res = None
		p1_set = set()
		p1 = parent_dict[v1]
		while p1 != None:
			p1_set.add(p1)
			p1 = parent_dict[p1]
		print('p1_set = ',p1_set)
		p2 = parent_dict[v2]
		while p2 != None:
			if p2 in p1_set:
				res = p2
				break
			p2 = parent_dict[p2]
		return res

	def LCA(self,v1,v2):
		if v1 == None or v2 == None:
			return None
		def LCA_util(root, v1,v2):
			if root == None:
				return None
			if root.value == v1 or root.value == v2:
				return root
			left_lca = LCA_util(root.left,v1,v2)
			right_lca = LCA_util(root.right,v1,v2)

			if left_lca and right_lca:
				return root
			if left_lca == None:
				return right_lca
			if right_lca == None:
				return left_lca
			return None

		lca = LCA_util(self.root,v1,v2)
		if lca != None:
			return lca.value
		else:
			return None


def sub_tree(root1,root2):
	if root1 == None:
		return (root2 == None)
	if root2 == None:
		return (root1 == None)

	def identical(root1,root2):
		if root1 == None:
			return (root2 == None)
		if root2 == None:
			return (root1 == None)

		return root1.value == root2.value and identical(root1.left,root2.left) and identical(root1.right,root2.right)

	if not identical(root1, root2):
		return sub_tree(root1.left,root2) or sub_tree(root1.right,root2)
	return True



n1 = Node(9,None,None)
tree = BST(n1)
tree.insert_value(5)
tree.insert_value(6)
tree.insert_value(15)
tree.insert_value(2)
tree.insert_value(3)
tree.insert_value(1)
tree.insert_value(18)
tree.in_order()
print('---is_balance---')
print(tree.is_balance())
print('find_height = ',tree.find_height())
print('--2nd tree--')
tree1 = BST()
tree1.insert_value(5)
tree1.insert_value(2)
tree1.insert_value(3)
tree1.insert_value(1)
print(tree1.in_order())
print('--1st tree and 2nd tree sub or not--')
print(sub_tree(tree.root,tree1.root))
print('--find_sum--')
print(tree.find_sum_path_withpath(14))
print(tree.find_sum_path_withpath(15))
print(tree.find_sum_path_withpath(7))
print(tree.find_sum_path_withpath(8))
print(tree.find_sum_path_withpath(11))
print('---find acestor---')
print(tree.find_acestor(2,18))
print(tree.LCA(2,18))
